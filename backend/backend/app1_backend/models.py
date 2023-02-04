from django.db import models
from django.contrib.auth.models import User
import pytesseract
from PIL import Image


# Create your models here.
class ExamImage(models.Model):
    image = models.ImageField(upload_to='app1_backend/images')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True)



    # def get_text(self):
    #     return pytesseract.image_to_string(Image.open(self.image.path))
