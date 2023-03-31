from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from application.models import databank
from friends.models import friends
from events.models import events
from blogs.models import blogbank
from recruiter.models import recruiter

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    queryset = friends.objects.all().order_by('-date_posted')
    eva = events.objects.all().order_by('-date_posted')
    bank = databank.objects.all().order_by('-date_posted')
    blogs = blogbank.objects.all().order_by('-date_posted')
    recrus = recruiter.objects.all().order_by('-date_posted')
    return render(request, 'users/profile.html',  {'queryset': queryset, 'bank':bank,'eva':eva, 'blogs':blogs,'recrus':recrus }, )