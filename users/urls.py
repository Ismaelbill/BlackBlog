from django.urls import path
from . import views

urlpatterns = [
    path('<str:user>/', views.user_profile, name='user_profile'),
    path('<str:user>/create-post/', views.create_post, name='create_post'),
    path('<str:username>/<int:id>', views.delete_acc, name='user_delete'),
    
]
