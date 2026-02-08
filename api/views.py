from rest_framework import viewsets, filters # filters: para filtrar os resultados da API
from django_filters.rest_framework import DjangoFilterBackend # DjangoFilterBackend: para filtrar os resultados da API
from shop.models import Category, Supplier, Product
from .serializers import CategorySerializer, SupplierSerializer, ProductSerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer   

class ProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer       

    # Configurações dos filtros da API
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # Filtro pela busca, que ordena e as opções de filtros do django (DjangoFilterBackend)
    # Campos filtrados
    filterset_fields = ["category", "supplier"] # Filtro para categoria e fornecedor
    # Campos Pesquisados
    search_fields = ["name", "description"] # Filtro para nome e descrição

    # Campos para ordenação
    ordering_fields = ["price","name", "stock"] # Filtro para ordenação por nome e preço