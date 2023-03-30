from rest_framework import serializers
from .models import Cart, Category, Order, Product


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product