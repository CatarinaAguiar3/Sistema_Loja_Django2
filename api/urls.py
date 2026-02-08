from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SupplierViewSet, ProductViewSet # views da API

# Imports do Swagger (Imports da Documnentação da API)
from rest_framework import permissions # permissions: traz premissões prontas
from drf_yasg.views import get_schema_view # Views do Swagger
from drf_yasg import openapi #Conjunto de paramentos para registrar a API na documentação do Swagger

schema_view = get_schema_view(
    openapi.Info(
        title="API da Loja Django",
        default_version="v1",
        description="API para gestão de produtos, categorias e fornecedores.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@loja.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"suppliers", SupplierViewSet)
router.register(r"products", ProductViewSet)


# Caminhos (Rotas)
urlpatterns = [
    path("", include(router.urls)), # Rota padrão da API
    
    # Rotas do Swagger (Rota da documentação da API)
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # Rotas do Redoc (Rota da documentação da API) -> Outra maneira de dcoumentação da API
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]