from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import *

class ImageManipulateViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageManipulateSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer




