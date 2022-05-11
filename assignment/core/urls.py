from django.urls import path
from .views import(
    get_all_products
)

urlpatterns = [
    path('get-all-products/', name='get-all-products',
         view=get_all_products),
]
