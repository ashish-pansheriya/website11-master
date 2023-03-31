from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import cashtreats
from application.models import databank
from friends.models import friends
from rest_framework import viewsets
from .serializers import rest

class restframe(viewsets.ModelViewSet):
    queryset = databank.objects.all()
    serializer_class = rest



def home(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        data = friends.objects.filter(address__icontains=q)

    return render(request, 'cashtreats/home.html', )

def terms(request):

    return render(request, 'cashtreats/terms.html', )


def about(request):
    return render(request, 'cashtreats/about.html', )

def policy(request):
    return render(request, 'cashtreats/policy.html', )

def services(request):
    return render(request, 'cashtreats/services.html', )


# def upload(request,user_id):
#     for afile in request.FILES.getlist('files'):
#         user = UserProfile.objects.get(user_id=user_id)
#         pic = UserProfile(request.POST or request.FILES)
#         pic.image = afile
#         pic.save()
#         redirect('upload')
#     else:
#
#         return render(request,'cashtreats/upload.html')