from django.urls import path, include
from blog import views

# app_name = 'post'

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/',views.PostCreateView.as_view(), name='post_new'),
    path('post/edit/<int:pk>/',views.PostUpdateView.as_view(), name='post_edit'),
    path('post/remove/<int:pk>/', views.PostDeleteView.as_view(), name='post_remove'),
    path('draft/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/comment/<int:pk>/',views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/approve/<int:pk>/', views.comment_approve, name='comment_approve'),
    path('comment/remove/<int:pk>/', views.comment_remove, name='comment_remove'),
    path('post/publish/<int:pk>/', views.post_publish, name='post_publish'),
]