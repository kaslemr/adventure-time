"""adventure_time URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken import views
<<<<<<< HEAD
from api_framework.views import api_respondent_detail_view, api_respondent_list_view, hello, RespondentListView, \
    RespondentDetailView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'respondent/', RespondentListView.as_view(), name="api_respondent_list_view"),
    url(r'respondent/?P<model_pk>\d+', RespondentDetailView.as_view(), name="api_respondent_detail_view")
=======

from rest_framework.authtoken import views
from api_framework.views import api_respondent_detail_view, api_respondent_list_view, hello, RespondentListView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api_framework.urls')),
>>>>>>> 6084a065a94fd10f7fa55bd7b94af6fa4925e088
]
