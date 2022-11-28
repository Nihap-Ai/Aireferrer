from django.contrib import admin
from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    path("", views.HomeView.as_view(), name="HomeView"),
    path("Art-Generator/", form, name="Art-Generator"),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('Art-output/', views.output, name='art_output'),
    path('Donate/', views.donate, name='donate'),



]
