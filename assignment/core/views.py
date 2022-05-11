from django.http import JsonResponse
from .models import Product


def get_all_products(request):
    products = Product.objects.all()
    ctx = {
        "products": []
    }
    for product in products:
        ctx['products'].append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price
        })

    return JsonResponse(ctx)
