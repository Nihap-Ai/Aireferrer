from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.HomeView.as_view(), name="HomeView"),
    path("Art-Generator/", form, name="Art-Generator"),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),

]
