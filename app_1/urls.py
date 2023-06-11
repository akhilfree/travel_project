from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('user_register/', views.user_register, name="user_register"),
    path('login/', views.login, name="login"),
    path('homepage/', views.homepage, name="homepage"),
    path('logout/', views.logout, name="logout"),
]