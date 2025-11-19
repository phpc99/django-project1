from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # '' is the root of the website, so it should be the home page
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]