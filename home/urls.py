from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post, name='post_detail'),
    path('post/<slug:slug>/<id>', views.post_delete, name='post_delete'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
]
