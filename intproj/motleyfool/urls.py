from django.urls import path
from . import views

urlpatterns = [
    #root path for index
    path('', views.index, name='index'),
    #article
    path('article/', views.content, name='article'),
]