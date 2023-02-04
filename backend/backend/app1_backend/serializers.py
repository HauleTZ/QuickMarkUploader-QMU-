from decimal import Decimal
from django.db import transaction
from rest_framework import serializers
from .models import *
import pytesseract
from PIL import Image
import cv2
# Cart, CartItem, Customer, Order, OrderItem, Product, Collection, ProductImage, Review



class ExamImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        image = validated_data['image']

        image = Image.open(image)
        print("image size(width, heigth) :", image.size)
      

        #crop image
        #box = (170, 170, 300, 300)
        #image = image.crop(box)
        # image - image.resize(263, 162)
        text = pytesseract.image_to_string(image)

        
        validated_data['text'] = text
        return ExamImage.objects.create(**validated_data)
    
    class Meta:
        model = ExamImage
        fields = '__all__'

     