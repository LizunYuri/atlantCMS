from django.urls import path
from . import views
from django.conf.urls import handler404
from django.shortcuts import render


urlpatterns = [
    path('submit-review-form/', views.submit_review_form, name='submit_review_form'),
    path('submit-client-form/', views.submit_client_form, name='submit_client_form'),
    path('', views.index, name='index'),
    path('politic/', views.politic, name='politic'),
    path('license/', views.license, name='license'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]



# Функция для обработки ошибки 404
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

# Укажите обработчик для 404 ошибок
handler404 = 'main.urls.custom_404_view'
