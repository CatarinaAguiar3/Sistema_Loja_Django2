from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category, Supplier
from .forms import ProductForm, SupplierForm, CategoryForm, UserForm

# Create your views here.
def product_list(request):
    produtos = Product.objects.all() # ORM  (Modelagem de Objetos Relacionais) # Aqui você pode buscar os produtos do banco de dados
    paginator = Paginator(produtos,3)

    page_number = request.GET.get("page")
    produtos = paginator.get_page(page_number)
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


# VIEW PARA CRIAR PRODUTO (FORMULÁRIO)
def product_create(request):
    if request.method == 'POST':

        #Se o MÉTODO for post, o formulário foi enviado
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save() # Salva o novo produto no BD
            return redirect('product_list')
    else:
        # Se o método for GET, exibe um formulário em branco
        form = ProductForm()

    return render(request, 'product_form.html', {'form': form})    


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_create')
    else:
        form = CategoryForm()

    return render(request, 'category_form.html', {'form': form})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_create')
    else:
        form = SupplierForm()

    return render(request, 'supplier_form.html', {'form': form})

# EDITAR PRODUTO
def product_update(request, pk): # Receber um request e o pk do produto a ser editado
    product = get_object_or_404(Product, pk=pk) # Se o produto existir, guarda ele. Caso não exista, mostra uma tela 404

    if request.method == 'POST': # Se o request for POST
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else: # Caso contrário, se o request for GET
        form = ProductForm(instance=product) # Preenche o form com os dados do produto que estão no Bnaco de dados

    return render(request, 'product_form.html', {'form': form})    

# DELETAR PRODUTO
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'product_confirm_delete.html', {'product': product})

# VIEW PARA CRIAR USUÁRIO (FORMULÁRIO)
def user_create(request):
    if request.method == 'POST': # Se o método for POST, significa que o usuário enviou o formulário preenchido
        form = UserForm(request.POST) # Pega os dados enviados no formulário
        if form.is_valid(): # Se o formulário for válido

            # cria o objeto mas não salva no banco ainda
            user =form.save(commit=False) # OBS: commit = False  -> cria um objeto na memória do servidor mas não salva no banco de dados
                                          #                         isso é importante pois dá uma chance de modificar o objeto antes de salvar 
                                          #                         (ou seja, para criptografar a senha antes de salvar)
            
            # criptografa a senha
            user.set_password(form.cleaned_data['password']) # OBS: form.cleaned_data['password'] -> pega a senha do formulário já validado (limpo) 
                                                             #                                     (a validação aconteceu no trecho: if form.is_valid() )
                                                             # OBS 2: set_password() -> função interna do modelo User do Django que criptografa a senha
                                                             #                          Essa função pega a senha em texto puro e a transforma em um hash
            user.save() # salva a senha criptografadano banco de dados
            return redirect('product_list') # depois de criar o usuário, redireciona a tela para a lista de produtos
    else: # Caso contrário, significa que o método foi GET, ou seja, o formulário foi enviado vazio (o usuário acabou de chegar na página)
        form = UserForm() # UserForm() -> cria um formulário vazio para o usuário preencher
    
    # Redireciona para o template user_form.html, enviando o formulário (form) seja vazio ou com erros de validação
    return render(request, 'user_form.html', {'form': form}) # OBS: Esta linha é executada tanto no caso de GET (formulário vazio) 
                                                             #      quanto no caso de POST com formulário inválido

# EDITAR CATEGORIA
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk) # busca categoria pelo ID (pk). Se não achar, retorna uma tela 404

    if request.method == 'POST': # Se o método for POST, o formulário foi enviado
        # preenche o formulário com os dados enviados e a instância da categoria
        form = CategoryForm(request.POST, instance=category) # usar "instance" para o Django saber que deve ATUALIZAR o formulário e 
                                                             # não criar um novo
        if form.is_valid(): # se o formulário for válido
            form.save() # salva as alterações no banco de dados
            return redirect('product_create')  # e depois, rediciona para a tela de criação de produto
    else: # Caso contrário, se o request for GET (apenas um acesso à página)
        form = CategoryForm(instance=category) # Preenche (Exibe) o form com os dados do produto que estão no Banco de dados

    # Enviar os dados da view para o template em forma de dicionário (context)
    return render(request, 'category_form.html', {'form': form})

# VIEW PARA SELECIONAR CATEGORIA E REDIRECIONAR PARA TELA DE EDIÇÃO
def category_select(request):
    category_id = request.GET.get('category_id') # Pega da URL o ID da categoria selecionada
    if category_id: # Se um ID da categoria existir
        return redirect('category_update', pk=category_id) # Redireciona o ID da categoria para a view 
                                                           # category_update (edição de categoria)
    return redirect('product_create') # Caso nenhuma categoria tenha sido selecionada, volta para a tela de criação de produto

# VIEW PARA PÁGINA PERSONALIZADA DE ERRO 404
def custom_page_not_found_view(request):
    # You can add custom logic here
    return render(request, "404.html", {"additional_context": "some_data"}, status=404) # status -> STATUS DE COMUNICAÇÃO HTTP (404 = Not Found)