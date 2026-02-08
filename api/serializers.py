from rest_framework import serializers
from shop.models import Category, Supplier,Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    # Passar todos os dados da categoria e fornecedor 
    #  category = CategorySerializer(read_only=True)
    #  supplier = SupplierSerializer(read_only=True) 

    # Otura maneira  
    #  category_name = serializers.ReadOnlyField(source='category_name')
    #  supplier_name = serializers.ReadOnlyField(source='supplier_name')


     class Meta:
          model = Product
          fields= "__all__"            