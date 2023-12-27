from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('main/', views.main, name = 'main'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('projects/', views.projects, name = 'projects'),
    path('products/', views.products, name = 'products'),
    path('news/',views.news, name = 'news'),
    path('vacancy/', views.vacancy, name = 'vacancy'),
]