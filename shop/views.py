from django.shortcuts import render
from .models import Product, Category, Supplier

# Create your views here.
def product_list(request):
    produtos = Product.objects.all() # ORM  (Modelagem de Objetos Relacionais) # Aqui você pode buscar os produtos do banco de dados
    return render(request, 'product_list.html', {'produtos': produtos}) # O produto retorna como uma lista

# Versão simples (sem filtro)
# # Create your views here.
# def teste(request):
#     produtos = Product.objects.all() # ORM  (Modelagem de Objetos Relacionais) # Aqui você pode buscar os produtos do banco de dados
#     categorias = Category.objects.all()
#     fornecedores = Supplier.objects.all()
#     return render(request, 'teste.html', {'produtos': produtos, 'categorias': categorias, 'fornecedores': fornecedores}) # O produto retorna como uma lista

# Versão com filtro
# Create your views here.
def teste(request): # request é o que o usuário envia para o servidor. Ou seja, é a requisição HTTP.
    produtos = Product.objects.all() # ORM  (Modelagem de Objetos Relacionais) # Aqui você pode buscar os produtos do banco de dados
    categorias = Category.objects.all()
    fornecedores = Supplier.objects.all()

    # Capturando Filtro usando "get" e "filter"
    #
    # Parâmetros da consulta: São uma forma de enviar dados para um servidor como parte de uma URL. 
    #                         Esses parâmtros são os valores que você quer filtrar ou buscar.
    #                         Exemplo: http://127.0.0.1:8000/teste/?chave1=valor1&chave2=valor2
    #
    # request.GET -> Pega os parâmetros da consulta e transforma em um dicionário. Ou seja, pega os dados da URL e trasnforma em um dicionário.
    #                Exemplo: chave1=valor1&chave2=valor2 -->  {'chave1': 'valor1', 'chave2': 'valor2'}
    #
    # request.GET.get() -> recupera os valores dos parâmetros. Se não existir valor, retorna None.
    #
    # Fonte: https://djangocentral.com/capturing-query-parameters-of-requestget-in-django/
    #
    nome = request.GET.get('nome')
    categoria_id = request.GET.get('categoria')
    fornecedor_id = request.GET.get('fornecedor')

    # Aplicando Filtros

    # Filtro por nome
    if nome:
        produtos = produtos.filter(name__icontains=nome)

    # Filtro por categoria
    if categoria_id:
        produtos = produtos.filter(category__id=categoria_id)   

    # Filtro por fornecedor
    if fornecedor_id:
        produtos = produtos.filter(supplier__id=fornecedor_id)        

    # Enviar os dados da view para o template em forma de dicionário (context)
    return render(request, 'teste.html', {'produtos': produtos, 'categorias': categorias, 'fornecedores': fornecedores}) # O produto retorna como uma lista