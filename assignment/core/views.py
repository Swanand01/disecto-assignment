import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Cart, CartProduct, Product


@api_view()
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

    return Response(ctx)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def test_view(request):
    return Response({
        "user": request.user.username
    })


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_cart(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    ctx = {
        "user": user.username,
        "products": []
    }
    for p in cart.products.all():
        ctx["products"].append({
            "name": p.product.name,
            "quantity": p.quantity
        })
    return Response(ctx)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_cart(request):
    if request.body:
        user = request.user
        cart = Cart.objects.get(user=user)
        updated_products = json.loads(request.body)["products"]
        for product in updated_products:
            p = Product.objects.get(name=product["name"])
            if cart.products.filter(product__name=product["name"]).exists():
                cp = cart.products.get(product__name=product["name"])
                cart.products.remove(cp)
                cp.delete()

                if product["quantity"] > 0:
                    newcp = CartProduct(
                        product=p, quantity=product["quantity"])
                    newcp.save()
                    cart.products.add(newcp)
            else:
                cp = CartProduct(product=p, quantity=product["quantity"])
                cp.save()
                cart.products.add(cp)
        return Response({"msg": "Cart updated successfully"})
