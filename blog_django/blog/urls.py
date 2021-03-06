from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name="post_list"),
    path('post/<int:pk', views.PostDetail.as_view(), name='post_detail'),
]