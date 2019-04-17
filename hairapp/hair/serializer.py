from rest_framework import serializers
from .models import Type, Hairstyle


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class HairstyleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hairstyle
        fields = '__all__'
