from django.shortcuts import render

# Create your views here.

# Home page
def home(request):
    return render(request, 'pages/home.html')

# About page
def about(request):
    return render(request, 'pages/about.html')

# Contact page
def contact(request):
    return render(request, 'pages/contact.html')