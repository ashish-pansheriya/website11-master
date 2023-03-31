from rest_framework import serializers
from application.models import databank


class rest(serializers.ModelSerializer):
    class Meta:
        model = databank
        fields = ['title', 'price', 'author','photo']
