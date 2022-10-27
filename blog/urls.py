from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page),
    path('new/', views.post_new),
    path('restaurants/', views.restaurants),
    path('restaurants/<int:pk>/', views.resingle_post_page),
    path('restaurants/re_new/',views.re_new),
    path('restaurants/re_new/',views.re_new),
]
