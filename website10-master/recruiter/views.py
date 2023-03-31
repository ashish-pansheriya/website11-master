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
class recruiterPostListView(ListView):
    model = recruiter
    template_name = 'recruiters/recruiters_home.html'
    context_object_name = 'post'  # it takes object in post for
    ordering = ['-date_posted']


BLOG_POST_PER_PAGE = 6
class recruitersearchview(View):

    def get(self,request,*args,**kwargs):
        queryset=recruiter.objects.all().order_by('-date_posted')
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(location__icontains=query) |
                Q(company__icontains=query) |
                Q(skill__icontains=query) |
                Q(job_details__icontains=query)
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
        return render(request, 'recruiters/recruiters_home.html', context )


class recruiterPostDetailView(DetailView):
    model = recruiter
    template_name = 'recruiters/recruiters_post_detail.html'


class recruiterPostCreateView(LoginRequiredMixin, CreateView):
    model = recruiter
    fields = ['name', 'designation', 'starts', 'ends', 'company', 'image', 'industry', 'location', 'job_title',
              'job_details', 'job_exp', 'skill', 'contact','email']
    template_name = 'recruiters/recruiters_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)


class recruiterPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # prevent from unauthorised update
    model = recruiter
    fields = ['name', 'designation', 'starts', 'ends', 'company', 'image', 'industry', 'location', 'job_title',
              'job_details', 'job_exp', 'skill', 'contact','email']
    template_name = 'recruiters/recruiters_post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # login must be required to run function with author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class recruiterPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # prevent from unauthorised update
    model = recruiter
    template_name = 'recruiters/recruiters_post_confirm_delete.html'
    success_url = '/recruiters-home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



