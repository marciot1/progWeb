# Adicione o import do método get_object_or_404 abaixo
from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
# Importe a classe UserUsuarioForm abaixo
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm
def list_usuario_view(request, id=None):
    # carrega somente usuarios, não inclui os admin
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
    'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)
    # adicione o método de edição
def edit_usuario_view(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    # Adicione as linhas a seguir
    # Perceba que os forms foram transferidos para dentro do if e do else
    emailUnused = True
    # Adicione a linha a seguir
    message = None
    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario)
        userForm = UserForm(request.POST, instance=request.user)
        # Verifica se o e-mail que o usuário está tentando utilizar
        # em seu perfil já existe em outro perfil
        verifyEmail = Usuario.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None
    else:
        usuarioForm = UserUsuarioForm(instance=usuario)
        userForm = UserForm(instance=request.user)
        if usuarioForm.is_valid() and userForm.is_valid() and emailUnused:
            usuarioForm.save()
            userForm.save()
            # Adicione a linha a seguir
            message = { 'type': 'success', 'text': 'Dados atualizados com sucesso' }
            # Adicione as linhas a seguir
        else:
            # Aqui verificamos se é do tipo post, para que na primeira vez que a página
            if request.method == 'POST':
                if emailUnused:
                    # Se o e-mail não está em uso tiver algum dado inválido.

                    message = { 'type': 'danger', 'text': 'Dados inválidos' }
                else:
                    # Se o e-mail já está em uso por outra pessoa.
                    message = { 'type': 'warning', 'text': 'E-mail já usado' }

                    # Até aqui
                    # Adicione a chave message a seguir
    context = {
        'usuarioForm': usuarioForm,
        'userForm': userForm,
        'message': message
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)