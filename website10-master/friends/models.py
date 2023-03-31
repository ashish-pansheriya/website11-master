from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from application .models import databank




class friends(models.Model):

    ages = (
        ('Choose one', 'Choose one'),
        ('till-20', 'till-20'),
        ('20-24', '20-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('55-64', '55-64'),
        ('65 or older', '65 or older'),
        ('I prefer to keep secret', 'I prefer to keep secret'),
    )


    type = (
        ('Choose one', 'Choose one'),
        ('Athletic/Muscular', 'Athletic/Muscular'),
        ('Slim/Slender', 'Slim/Slender'),
        ('Average', 'Average'),
        ('A little above average', 'A little above average'),
        ('Full Figured', 'Full Figured'),
    )
    heights = (
        ('Choose one', 'Choose one'),
        ('Very Short', 'Very Short'),
        ('Short', 'Short'),
        ('Average', 'Average'),
        ('Above Average', 'Above Average'),
        ('Tall', 'Tall'),
    )
    fee = (
        ('negotiable', 'negotiable'),
        ('$10 hour', '$10 hour'),
        ('$20 hour', '$20 hour'),
        ('$30 hour', '$30 hour'),
        ('$40 hour', '$40 hour'),
        ('$50+ hour', '$50+ hour'),
    )
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=100, null=True, verbose_name='Nickname')
    age = models.CharField(max_length=100, null=True, default='Choose one', choices=ages, verbose_name='What is your age?')
    activities = models.CharField(max_length=200, null=True, default='I am up for ', verbose_name='Available for, Business Events, Parties, Yoga, Movies, Music, Hanging Out, Religious, Swimming, Workout Partner etc or I am Up For Everything')
    gender = models.CharField(max_length=20, null=True, choices=gender_choices, verbose_name='Gender')
    body = models.CharField(max_length=200, null=True, choices=type, default='Choose one', verbose_name='Body Type')
    height = models.CharField(max_length=50, null=True, choices= heights, default='Choose one', verbose_name='Height')
    about = models.TextField(max_length=400, default='The best thing about me is ', null=True, verbose_name='A short description about yourself')
    language = models.CharField(max_length=100, default='English, ', null=True,verbose_name='Languages | Speak')
    address = models.CharField(max_length=100, null=True, verbose_name='Your Location')
    fees = models.CharField(max_length=50, choices=fee, default='negotiable', null=True, verbose_name='My fees')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.IntegerField(null=True, verbose_name='Phone Number')
    email = models.EmailField(max_length=50, null=True, verbose_name='Email id')
    photo = models.ImageField(upload_to='media', null=True, verbose_name='Profile Picture,')


    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('friend-post-detail', kwargs={'pk': self.pk})


class frienddata(forms.ModelForm):

    class Meta:
        model = friends
        fields = ['name', 'age', 'activities', 'gender', 'body', 'height', 'fees', 'language','contact', 'email', 'address', 'about', 'photo']




class Images(models.Model):
    post = models.ForeignKey(friends, default=None, null=True, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='media', null=True, verbose_name='Profile Picture,')

    def __str__(self):
        return str(self.file)


class friend(forms.ModelForm):

    class Meta:
        model = Images
        fields = ['file']

