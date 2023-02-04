from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
import pytesseract
from PIL import Image


# Create your views here.
class ExamImageViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    queryset = ExamImage.objects.all()
    serializer_class = ExamImageSerializer



 


