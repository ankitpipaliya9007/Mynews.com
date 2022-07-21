from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path('', views.news1),
    path('news/', views.news1),
    path('news/<data>', views.news)
]
