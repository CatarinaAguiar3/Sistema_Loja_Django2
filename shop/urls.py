from django.urls import path
from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("teste/", views.teste, name="teste"),
    path("create_product/", views.product_create, name="product_create"), # rota para tela que cria produto
    path("create_category/", views.category_create, name="category_create"),
    path("create_supplier/", views.supplier_create, name="supplier_create"),
    path("edit_product/<int:pk>/", views.product_update, name="product_update"),
    path("delete_product/<int:pk>/", views.product_delete, name="product_delete"),
    path("create_user/", views.user_create, name="user_create"), # rota para tela que cria usuário
    path("edit_category/<int:pk>/", views.category_update, name="category_update"),
    path("category_select/", views.category_select, name="category_select"),
]

# Rotas Curingas
# Página quando encontra error 404
handler404 = "shop.views.custom_page_not_found_view"