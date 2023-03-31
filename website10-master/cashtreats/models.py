from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cashtreats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name='Owner')
    phone_no = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=244, null=True)
    country = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=20, null=True)
    user_image = models.ImageField(upload_to='user_image')

    def __str__(self):
        return self.city

#
# class Image(models.Model):
#    user = models.ForeignKey(cashtreats, on_delete=models.CASCADE, null=True, verbose_name='Owner')
#    image = models.ImageField(upload_to='user_images')