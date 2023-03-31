from django.shortcuts import render
from django.http import HttpResponse
import time
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.core.files.storage import FileSystemStorage
from django.forms import formset_factory
#from .filters import friendsFilter
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import friends
stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request):
    if request.method == 'POST':
        # Get the token from the form data
        token = request.POST.get('stripeToken')

        # Charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=2000,  # amount in cents
                currency='cad',
                description='Monthly Subscription',
                source=token,
            )
        except stripe.error.CardError as e:
            # The card has been declined
            pass

        return render(request, 'success.html')

    # Render the payment form template
    stripe.api_key = settings.STRIPE_SECRET_KEY
    context = {'stripe_key': settings.STRIPE_PUBLISHABLE_KEY}
    return render(request, 'payment.html', context)




def filter(request):

    context = {'AAAA':'AAAA'}
    return render(request, 'cashtreats/stuff.html', {'context':context})

class ItemCreation(CreateView):
    template_name = "friends/modelform.html"
    model = friends
    form_class = frienddata
    success_url = 'home'
#     def get_context_data(self,**kwargs,request):
#         photos = friends.objects.all()
#         formv = frienddata(request.POST)
#         if formv.is_valid():
#             formv.save()
#             return HttpResponseRedirect('/')
#         else:
#             formv = frienddata()
#         return render(request, 'friends/modelform.html', {'formv': formv})
#

def geter(request):
    photos = friends.objects.all()
    formv = frienddata(request.POST)
    if formv.is_valid():
        formv.save()
        return HttpResponseRedirect('/')
    else:
        formv = frienddata()
    return render(request, 'friends/modelform.html', {'formv':formv})


class ProgressBarUploadView(LoginRequiredMixin, CreateView):
    def get(self, request):
        formv = frienddata(self.request.POST)
        if formv.is_valid():
            formv.save()
            return HttpResponseRedirect('friend-home')
        else:
            formv = frienddata()
        return render(request, 'friends/new.html', {'formv':formv})

    def post(self, request):
        form = friend(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        formv = frienddata(request.POST)
        if formv.is_valid():
            formv.save()
            return HttpResponseRedirect('friend-home')
        else:
            formv = frienddata()
        return JsonResponse(data)


######
class friendPostListView(ListView):
    model = friends
    template_name = 'friends/friends_home.html'
    context_object_name = 'post'  # it takes object in post for
    ordering = ['-date_posted']


BLOG_POST_PER_PAGE = 8

class Searchview(View):

    def get(self, request, *args, **kwargs):

        queryset = friends.objects.all().order_by('-date_posted') # ordering latest first
        query = request.GET.get('q')
        queryradio = request.GET.get('gender')
        alll = request.GET.get('all')
        if query:
            queryset = queryset.filter(Q(address__icontains=query)).distinct()
        if queryradio:
            queryset = queryset.filter(
                Q(gender__startswith=queryradio)
            ).distinct()
        if alll:
            queryset=queryset.filter(
                Q(gender__icontains=alll)
            ).distinct()


        page = request.GET.get('page', 1)
        blog_posts_paginator = Paginator(queryset, BLOG_POST_PER_PAGE)
        try:
            queryset = blog_posts_paginator.page(page)
        except PageNotAnInteger:
            queryset = blog_posts_paginator.page(BLOG_POST_PER_PAGE)
        except EmptyPage:
            queryset = blog_posts_paginator.page(blog_posts_paginator.num_pages)

        context = {
            'queryset': queryset,
        }
        return render(request, 'friends/friends_home.html', context )

#search_result.html



class friendPostDetailView(DetailView):
    model = friends
    template_name = 'friends/friends_post_detail.html'


class friendPostCreateView(LoginRequiredMixin, CreateView):

    model = friends
    fields = ['name', 'age', 'activities', 'gender', 'body', 'height', 'fees', 'language','contact', 'email', 'address', 'about', 'photo']
    template_name = 'friends/friends_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)


class friendPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # prevent from unauthorised update
    model = friends
    fields = ['name', 'age', 'activities', 'gender', 'body', 'height', 'fees', 'language', 'contact', 'email',
              'address', 'about', 'photo']
    template_name = 'friends/friends_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class friendPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # prevent from unauthorised update
    model = friends
    template_name = 'friends/friends_post_confirm_delete.html'
    success_url = '/friend-home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

##########################################################################################

# class FriendCreateView(LoginRequiredMixin, CreateView ):
#     model = friends
#     fields = ['name', 'age','title']
#     template_name = 'friends/upload2.html'
#     success_url = 'friends'
#     def form_valid(self, form):
#         form.instance.author = self.request.user #login must be required to run function with author
#         return super().form_valid(form)
#
#
# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'friends/upload2.html'  # Replace with your template.
#     success_url = 'upload2'  # Replace with your URL or reverse().
#
#     def add(request):
#         if request.method == 'POST':  # If the form has been submitted...
#             form = FileFieldForm(request.POST)  # A form bound to the POST data
#             if form.is_valid():
#                 form.save()
#         return HttpResponse('Saved')
#
#
#
#
#
#
# def friends_list(request):
#     if request.method == 'POST':
#         form = formfriends(request.POST or request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Saved')
#     else:
#         form = formfriends()
#     return render(request, 'friends/friends_list.html', {"form":form})
# #
# #
# def friends_details(request):
#     return render(request, 'friends/friends_details.html', {"text":"text"})
