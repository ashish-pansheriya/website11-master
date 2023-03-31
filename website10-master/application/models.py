from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class databank(models.Model):

    categories = (
        ('Buy & Sell', 'Buy & Sell'),
        ('Cars & Vehicles', 'Cars & Vehicles'),
        ('Real Estate', 'Real Estate'),
        ('Mobiles', 'Mobiles'),
        ('Furniture', 'Furniture'),
        ('Bikes', 'Bikes'),
        ('Jobs', 'Jobs'),
        ('Services', 'Services'),
        ('Community', 'Community'),
        ('Vacation Rentals', 'Vacation Rentals'),
    )
    title = models.CharField(max_length=100, verbose_name='Ad title')
    category = models.CharField(max_length=20, null=True, choices=categories, default='01', verbose_name='Select a category')
    content = models.TextField(max_length=400, null=True, verbose_name='Description')
    price = models.CharField( max_length=50,  null=True, verbose_name='Price (Be specific with currency type & amount)')
    location = models.CharField(max_length=100, null=True, verbose_name='Location')
    contact = models.IntegerField( null=True, verbose_name='Phone Number (Your phone number will show up on your Ad.)')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email (Your email address will not be shared with others.)')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    owner = models.CharField(max_length=17, null=True, verbose_name="Name of the owner")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Owner')
    photo = models.ImageField(upload_to='media', verbose_name='Photo')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
