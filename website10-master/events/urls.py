
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [


    path('events', events, name='events'),
    path('event-home', eventsearchview.as_view(), name='event-home'),
    #path('event-home', eventPostListView.as_view(), name='event-home'),
    path('event/<int:pk>/', eventPostDetailView.as_view(), name='event-post-detail'),
    path('event/new/', eventPostCreateView.as_view(), name='event-post-create'),
    path('event/<int:pk>/update/', eventPostUpdateView.as_view(), name='event-post-update'),
    path('event/<int:pk>/delete/', eventPostDeleteView.as_view(), name='event-post-delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

