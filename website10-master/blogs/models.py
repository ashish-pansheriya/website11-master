from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class blogbank(models.Model):

    categories = (
        ('Spiritual Blog', 'Spiritual Blog'),
        ('Dating Blog', 'Dating Blog'),
        ('Love Blog', 'Love Blog'),
        ('Friends Blog', 'Friends Blog'),
        ('Fashion Blog', 'Fashion Blog'),
        ('Food Blog', 'Food Blog'),
        ('Travel Blog', 'Travel Blog'),
        ('Music Blog', 'Music Blog'),
        ('Lifestyle Blog', 'Lifestyle Blog'),
        ('Fitness Blog', 'Fitness Blog'),
        ('DIY Blog', 'DIY Blog'),
        ('Sports Blog', 'Sports Blog'),
        ('Finance Blog', 'Finance Blog'),
        ('Political Blog', 'Political Blog'),
        ('Parenting Blog', 'Parenting Blog'),
        ('Business Blog', 'Business Blog'),
        ('Personal Blog', 'Personal Blog'),
        ('Movie Blog', 'Movie Blog'),
        ('Car Blog', 'Car Blog'),
        ('News Blog', 'News Blog'),
        ('Pet Blog', 'Pet Blog'),
        ('Gaming Blog', 'Gaming Blog'),
        ('Technology Blog', 'Technology Blog'),
        ('Religious Blog', 'Religious Blog'),
        ('Story Blog', 'Story Blog'),
        ('Blog', 'Blog')
    )
    title = models.CharField(max_length=300, verbose_name='Blog Title')
    category = models.CharField(max_length=20, null=True, choices=categories, default='Blog', verbose_name='Blog About')
    content = RichTextField()
    photo = models.ImageField(upload_to='media', verbose_name='Blog Image')
    name = models.CharField( max_length=50,  null=True, verbose_name='Creator Name')
    email = models.EmailField(max_length=50, null=True, verbose_name='Creator Email')
    location = models.CharField(max_length=100, null=True, verbose_name='Location')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Posted')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Owner')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
