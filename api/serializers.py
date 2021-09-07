from rest_framework import serializers

from .models import Ingredient

class Ingredient(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"