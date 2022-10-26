from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.HomeView.as_view(), name="HomeView"),
    path("form/", form, name="form"),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),

]
