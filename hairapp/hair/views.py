from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Type,Hairstyle
from .serializer import TypeSerializer,HairstyleSerializer

class ListTypeView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
# Create your views here.
class ListHairstyleView(generics.ListAPIView):
    queryset = Hairstyle.objects.all()
    serializer_class = HairstyleSerializer
# Create your views here.

def my_view(request):
    hair_serializer = HairstyleSerializer(hair, context={"request":request})
    hair_serializer.data
    
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
