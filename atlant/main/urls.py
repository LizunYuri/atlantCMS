from django.urls import path
from . import views



urlpatterns = [
    path('submit-client-form/', views.submit_client_form, name='submit_client_form'),
    path('', views.index, name='index'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]