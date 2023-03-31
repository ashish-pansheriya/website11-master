from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from django.core.files.storage import FileSystemStorage
from django.forms import formset_factory
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

######
class eventPostListView(ListView):
    model = events
    template_name = 'events/events_home.html'
    context_object_name = 'post'  # it takes object in post for
    ordering = ['-date_posted']


BLOG_POST_PER_PAGE = 6
class eventsearchview(View):

    def get(self,request,*args,**kwargs):
        queryset=events.objects.all().order_by('-date_posted')
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(location__icontains=query) |
                Q(title__icontains=query) |
                Q(types__icontains=query) |
                Q(topic__icontains=query)
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
            'queryset':queryset
        }
        return render(request, 'events/events_home.html', context )


class eventPostDetailView(DetailView):
    model = events
    template_name = 'events/events_post_detail.html'


class eventPostCreateView(LoginRequiredMixin, CreateView):
    model = events
    fields = ['title', 'location', 'types', 'topic', 'starts', 'ends', 'image', 'description', 'organiser',
              'description2', 'tickets', 'contact', 'email']
    template_name = 'events/events_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)


class eventPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # prevent from unauthorised update
    model = events
    fields = ['title', 'location', 'types', 'topic', 'starts', 'ends', 'image', 'description', 'organiser',
              'description2', 'tickets', 'contact', 'email']
    template_name = 'events/events_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class eventPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # prevent from unauthorised update
    model = events
    template_name = 'events/events_post_confirm_delete.html'
    success_url = '/events-home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



