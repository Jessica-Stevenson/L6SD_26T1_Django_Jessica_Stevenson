from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'board/home.html') 

def about_view(request):
    return HttpResponse("This is the About Page.")

def notices_view(request):
    return HttpResponse("Here are the latest notices.")