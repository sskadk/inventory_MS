from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ProductType
from .serializers import ProductTypeSerializer

class ProductTypeApiView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
