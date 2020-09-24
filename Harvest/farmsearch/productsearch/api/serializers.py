from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'price',
            'date_created',
            'date_updated',
            'quantity',
            'in_stock',
        )

