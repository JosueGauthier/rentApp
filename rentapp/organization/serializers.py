from rest_framework import serializers

from reservation.views import check_reservation_for_non_consumable

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
    check_reservation_for_non_consumable()
    class Meta:
        model = Product
        fields = ['id', 'name_product', 'image_product_url', 'category',
                  'is_active', 'is_removed', 'qty_total', 'qty_available', 'is_consumable', ]




class CreateProductSerializer(serializers.Serializer):
    """
    
    """

    product_name = serializers.CharField(
        write_only=True
    )

    price_is_manual = serializers.BooleanField(
        write_only=True
    )

    manual_price = serializers.DecimalField(
        write_only=True,
        decimal_places=2,
        max_digits=9,
    )
    shop_id = serializers.IntegerField(
        write_only=True,
    )

    is_active = serializers.BooleanField(
        write_only=True
    )

    product_unit = serializers.CharField(
        write_only=True,
        required=False

    )

    correcting_factor = serializers.DecimalField(
        write_only=True,
        decimal_places=4,
        max_digits=9,
    )

    product_image = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        product_name = attrs.get('product_name')
        price_is_manual = attrs.get('price_is_manual')
        manual_price = attrs.get('manual_price')
        shop_id = attrs.get('shop_id')
        is_active = attrs.get('is_active')
        product_unit = attrs.get('product_unit')
        correcting_factor = attrs.get('correcting_factor')
        product_image = attrs.get('product_image')

        attrs['product'] = [product_name, price_is_manual,
                            manual_price, shop_id, is_active, product_unit, correcting_factor, product_image]
        return attrs


class UpdateProductSerializer(serializers.Serializer):
    """
    :type name: string
    :type is_manual: bool
    :type manual_price: decimal
    :type is_active: bool
    :type unit: string
    :type correcting_factor: decimal
    :type product_image : string

    """

    product_id = serializers.CharField(
        write_only=True
    )

    product_name = serializers.CharField(
        write_only=True, required=False

    )

    price_is_manual = serializers.BooleanField(
        write_only=True, required=False
    )

    manual_price = serializers.DecimalField(
        write_only=True,
        decimal_places=2,
        max_digits=9,
        required=False,
    )

    is_active = serializers.BooleanField(
        write_only=True
    )

    product_unit = serializers.CharField(
        write_only=True,
        required=False,
    )

    correcting_factor = serializers.DecimalField(
        write_only=True,
        decimal_places=4,
        max_digits=9,
        required=False
    )

    product_image = serializers.CharField(
        write_only=True,
        required=False
    )

    def validate(self, attrs):

        product_id = attrs.get('product_id')
        product_name = attrs.get('product_name')
        price_is_manual = attrs.get('price_is_manual')
        manual_price = attrs.get('manual_price')
        is_active = attrs.get('is_active')
        product_unit = attrs.get('product_unit')
        correcting_factor = attrs.get('correcting_factor')
        product_image = attrs.get('product_image')

        attrs['product'] = [product_id, product_name, price_is_manual,
                            manual_price, is_active, product_unit, correcting_factor, product_image]
        return attrs


class DeleteProductSerializer(serializers.Serializer):
    """
    """

    product_id = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        product_id = attrs.get('product_id')
        attrs['product'] = [product_id]
        return attrs
