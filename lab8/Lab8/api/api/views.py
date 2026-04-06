from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Product


def product_list(request):
    products = Product.objects.filter(is_active=True, count__gt=0).order_by('count')
    data = {
        'products': list(products.values())
    }
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        return JsonResponse({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description,
            "count": product.count,
            "is_active": product.is_active,
            "category_id": product.category_id
        }, json_dumps_params={'ensure_ascii': False})
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)


def category_list(request):
    categories = Category.objects.all()
    return JsonResponse({
        "categories": list(categories.values())
    }, safe=False, json_dumps_params={'ensure_ascii': False})


def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, json_dumps_params={'ensure_ascii': False})
    except Category.DoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=404)


def products_by_category(request, id):
    try:
        category = Category.objects.get(id=id)
        
        products = category.products.filter(is_active=True, count__gt=0).order_by('count')

        return JsonResponse({
            "products": list(products.values())
        }, safe=False, json_dumps_params={'ensure_ascii': False})
    except Category.DoesNotExist:
        return JsonResponse({"error": "Category not found"}, status=404)