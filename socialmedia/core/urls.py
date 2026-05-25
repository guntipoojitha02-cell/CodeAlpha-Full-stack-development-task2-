from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),

    path('profile/<int:id>/', views.profile),

    path('create-post/', views.create_post),

    path('like/<int:id>/', views.like_post),

    path('comment/<int:id>/', views.add_comment),

    path('follow/<int:id>/', views.follow_user),

]