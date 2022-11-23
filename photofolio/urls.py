from django.urls import  path
from . import views

urlpatterns=[
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('login', views.login_user_or_admin, name="login"),
    path('upload', views.upload, name="upload"),
    path('register', views.register, name='register'),
    path('gallery/<str:pk>', views.gallery, name='gallery'),
    path('galleryinner', views.galleryinner, name='galleryinner'),
    path('logout', views.logout_user_or_admin, name='logout'),

]