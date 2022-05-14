from django.urls import path
from .views import(
    get_all_products,
    create_new_order,
    place_order,
    test_view,
    get_order,
    update_order,
    generate_invoice
)

urlpatterns = [
    path('get-all-products/', name='get-all-products',
         view=get_all_products),
    path('test-view/', name='test', view=test_view),
    path('create-new-order/', name='create-new-order', view=create_new_order),
    path('get-order/<str:order_id>', name='get-order', view=get_order),
    path('update-order/<str:order_id>', name='update-order', view=update_order),
    path('place-order/<str:order_id>', name='place-order', view=place_order),
    path('generate-invoice/<str:order_id>',
         name='generate-invoice', view=generate_invoice)
]
