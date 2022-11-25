from rest_framework import serializers

from .models import *


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name_organization', 'image_organization_url']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_category', 'image_category_url', 'organization',]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name_product', 'image_product_url', 'category',
                  'is_active', 'is_removed', 'qty_total', 'qty_available', 'is_consumable', ]
