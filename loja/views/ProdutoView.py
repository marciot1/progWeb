from django.http import HttpResponse
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone

def list_produto_view(request, id=None):
  # Carrega do navegador as opções de filtragem
  produto = request.GET.get("produto")
  destaque = request.GET.get("destaque")
  promocao = request.GET.get("promocao")
  categoria = request.GET.get("categoria")
  fabricante = request.GET.get("fabricante")
  # Carrega do banco de dados todos proutos
  #produtos = Produto.objects.filter(Produto=produto)
  produtos = Produto.objects.all()
  if produto is not None:
    #produtos = produtos.filter(Produto=produto)
    produtos = produtos.filter(Produto__contains=produto )
  if promocao is not None:
    produtos = produtos.filter(promocao=promocao)
  if destaque is not None:
    produtos = produtos.filter(destaque=destaque)
  #if categoria is not None:
  #  produtos = produtos.filter(categoria=categoria)
  #if fabricante is not None:
  #  produtos = produtos.filter(fabricante=fabricante)
  if categoria is not None:
    produtos = produtos.filter(categoria__Categoria=categoria)
  if fabricante is not None:
    produtos = produtos.filter(fabricante__Fabricante=fabricante)    
  if id is not None:
    produtos = produtos.filter(id=id)

  now = timezone.now()
  now = now - timedelta(days = int(1))
  #produtos = produtos.filter(criado_em__gte=now)

  # Mostra os produtos consultados
  print(produtos)
  ## Visualizar os parametros que retornam do navegador
  if destaque is not None:
    print(destaque)
  if produto is not None:
    print(produto)
  if promocao is not None:
    print(promocao)
  if categoria is not None:
    print(categoria)
  if fabricante is not None:
    print(fabricante)
  if id is None:
    return HttpResponse('<h1>Nenhum id foi informado</h1>')
  return HttpResponse('<h1>Produto de id %s!</h1>' % id)