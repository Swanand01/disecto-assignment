import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order, OrderProduct, Product


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
def get_order(request):
    user = request.user
    order = Order.objects.get(user=user)
    ctx = {
        "user": user.username,
        "products": []
    }
    for p in order.products.all():
        ctx["products"].append({
            "name": p.product.name,
            "quantity": p.quantity
        })
    return Response(ctx)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_order(request):
    if request.body:
        user = request.user
        order = Order.objects.get(user=user)
        updated_products = json.loads(request.body)["products"]
        for product in updated_products:
            p = Product.objects.get(name=product["name"])
            if order.products.filter(product__name=product["name"]).exists():
                # Implement get_or_create()
                cp = order.products.get(product__name=product["name"])
                order.products.remove(cp)
                cp.delete()

                if product["quantity"] > 0:
                    newcp = OrderProduct(
                        product=p, quantity=product["quantity"])
                    newcp.save()
                    order.products.add(newcp)
            else:
                cp = OrderProduct(product=p, quantity=product["quantity"])
                cp.save()
                order.products.add(cp)
        return Response({"msg": "Order updated successfully"})
