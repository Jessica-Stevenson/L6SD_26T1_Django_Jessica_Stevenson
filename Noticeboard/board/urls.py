# board/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),        # /board/ or /
    path('about/', views.about_view, name='about'), # /board/about/
    path('notices/', views.notices_view, name='notices'), # /board/notices/
]