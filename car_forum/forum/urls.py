from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Forum-home"),
    path('about/', views.about, name="Forum-about"),
    path('Mycar/', views.about, name="Forum-Mycar"),
    path('register/', views.about, name="Forum-register"),
]
