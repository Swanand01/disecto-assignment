from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Cart


class CustomRegisterSerializer(RegisterSerializer):
    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        Cart(user=user).save()
        return user
