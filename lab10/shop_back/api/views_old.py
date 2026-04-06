from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # GET /api/categories/<id>/products/
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        products = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['delete'])
    def delete_by_status(self, request):
        status_to_delete = request.data.get('is_active', False)

        Product.objects.filter(is_active=status_to_delete).delete()

        active_products = Product.objects.filter(is_active=True).order_by('price')
        serializer = ProductSerializer(active_products, many=True)
        return Response(serializer.data)