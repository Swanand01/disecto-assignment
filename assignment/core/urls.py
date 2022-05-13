from django.urls import path
from .views import(
    get_all_products,
    test_view,
    get_cart,
    update_cart
)

urlpatterns = [
    path('get-all-products/', name='get-all-products',
         view=get_all_products),
    path('test-view/', name='test', view=test_view),
    path('get-cart/', name='get-cart', view=get_cart),
    path('update-cart/', name='update-cart', view=update_cart)
]
