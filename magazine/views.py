from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from .permissions import IsAdminUserOrReadOnly, IsClientReadOnlyOrAdminUser
from .models import Order, Category, Cart, Product
from .serializers import OrderSerializer, CategorySerializer, CartSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated


# Product CRUD
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUserOrReadOnly])
def ProductListView(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"data": serializer.data}, status=HTTP_200_OK)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "product_id": serializer.data['id'],
                "message": "Product was added!"
            }
            return Response(data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@permission_classes([IsAdminUserOrReadOnly])
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def ProductDetailView(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response({"error": "This product is not available"}, status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product removed"})


# Category CRUD
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUserOrReadOnly])
def CategoryListView(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"data": serializer.data}, status=HTTP_200_OK)
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "category_id": serializer.data['id'],
                "message": "Category was added!"
            }
            return Response(data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAdminUserOrReadOnly])
def CategoryDetailView(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except:
        return Response({"error": "This category is not available"}, status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        category.delete()
        return Response({"message": "Category removed"})


# Order CRUD
@api_view(['GET', 'POST'])
@permission_classes([IsClientReadOnlyOrAdminUser])
def OrderListView(request):
    if request.method == 'GET':
        products = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(products, many=True)
        return Response({"data": serializer.data}, status=HTTP_200_OK)
    if request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "order_id": serializer.data['id'],
                "message": "Order was added!"
            }
            return Response(data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsClientReadOnlyOrAdminUser])
def OrderDetailView(request, pk):
    try:
        order = Order.objects.get(pk=pk, user=request.user)
    except:
        return Response({"error": "This order is not available"}, status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        order.delete()
        return Response({"message": "Order removed"})


# Order CRUD
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def CartListView(request):
    if request.method == 'GET':
        cart = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(cart, many=True)
        return Response({"data": serializer.data}, status=HTTP_200_OK)
    if request.method == "POST":
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "cart_id": serializer.data['id'],
                "message": "Cart was added!"
            }
            return Response(data, status=HTTP_201_CREATED)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def CartDetailView(request, pk):
    try:
        cart = Cart.objects.get(pk=pk, user=request.user)
    except:
        return Response({"error": "This cart is not available"}, status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        cart.delete()
        return Response({"message": "Cart removed"})
