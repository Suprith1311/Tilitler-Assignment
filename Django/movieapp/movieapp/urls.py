from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from pip._internal.models import index
from rest_framework.urlpatterns import format_suffix_patterns
from movieapi import views

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'', TemplateView.as_view('template_name='index.html))
]
