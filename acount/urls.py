from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registerUser, name='registerUser'),
    path('login/', views.loginUser, name='loginUser'),
    path('home/', views.homePage, name='homePage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('contact/', views.contactUsPage, name='contactUs'),
    path('aboutProj/', views.aboutProject, name='aboutProj'),
]