from rest_framework import serializers
from .models import MenuItem, Category

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']
class MenuItemSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)
    Category = CategorySerializer(read_only=True)

    class Meta:
        model = MenuItem
        fields = [
            'id',
            'title',
            'price',
            'inventory',
            'category',
            'category_id',
            'Category',  # ✅ ADD THIS LINE
        ]
