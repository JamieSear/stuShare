from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='share-home'),
    path('about/', views.about, name='share-about'),
]