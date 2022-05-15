import json
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Order, OrderProduct, Product


@api_view(["GET"])
def get_all_products(request):
    """
    Return JSON Response containing all products.
    """
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
def get_order(request, order_id):
    """
    Gets Order from order_id.
    Returns JSON Response containing name, quantity of all OrderProducts in that order.
    """
    user = request.user
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"msg": "Order does not exist."})

    if not order.user == user:
        return Response({"msg": "Unauthorised"})

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


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_order(request, order_id):
    """
    Update an Order.
    Gets the Order from order_id, and updates its OrderProducts with the ones sent in the request.
    """
    if not request.body:
        return Response({"msg": "Request body cannot be empty."})

    user = request.user

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"msg": "Order does not exist."})

    if not order.user == user:
        return Response({"msg": "Unauthorised"})

    data = json.loads(request.body)

    if not "products" in data.keys():
        return Response({"msg": "products list not found."})

    updated_products = data["products"]
    if len(updated_products) == 0:
        return Response({"msg": "products list cannot be empty"})

    for product in updated_products:
        p = Product.objects.get(name=product["name"])
        if order.products.filter(product__name=product["name"]).exists():
            op = order.products.get(product__name=product["name"])
            order.products.remove(op)
            op.delete()

            if product["quantity"] > 0:
                newcp = OrderProduct(
                    product=p, quantity=product["quantity"])
                newcp.save()
                order.products.add(newcp)
        else:
            op = OrderProduct(product=p, quantity=product["quantity"])
            op.save()
            order.products.add(op)
    return Response({"msg": "Order updated successfully"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_new_order(request):
    """
    Creates a new Order with the OrderProducts sent in the request.
    """
    if not request.body:
        return Response({"msg": "Request body cannot be empty."})

    data = json.loads(request.body)

    if not "products" in data.keys():
        return Response({"msg": "products list not found."})

    products = data["products"]

    if len(products) == 0:
        return Response({"msg": "products list cannot be empty"})

    user = request.user
    order = Order(user=user)
    order.save()

    for product in products:
        p = Product.objects.get(name=product["name"])
        op = OrderProduct(product=p, quantity=product["quantity"])
        op.save()
        order.products.add(op)

    return Response({"msg": "Order created successfully."})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def place_order(request, order_id):
    """
    Changes Order status to placed.
    """
    user = request.user
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({"msg": "Order does not exist."})

    if not order.user == user:
        return Response({"msg": "Unauthorised"})

    if list(order.products.all()):
        order.is_placed = True
        order.save()
        return Response({"msg": "Order placed successfully"})


def generate_invoice(request, order_id):
    """
    View to generate invoice for an Order.
    """
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return JsonResponse({"msg": "Order does not exist."})

    ctx = {
        "name": order.user.username,
        "order_id": order.id,
        "products": []
    }
    total = 0
    for product in order.products.all():
        ctx["products"].append({
            "name": product.product.name,
            "price_per_unit": product.product.price,
            "quantity": product.quantity,
            "total": product.product.price * product.quantity
        })
        total += product.product.price * product.quantity

    ctx["total"] = total
    return render(request, "invoice_template.html", ctx)
