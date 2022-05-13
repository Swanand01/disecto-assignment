from django.urls import path
from .views import(
    get_all_products,
    test_view,
    get_order,
    update_order
)

urlpatterns = [
    path('get-all-products/', name='get-all-products',
         view=get_all_products),
    path('test-view/', name='test', view=test_view),
    path('get-order/', name='get-order', view=get_order),
    path('update-order/', name='update-order', view=update_order)
]
