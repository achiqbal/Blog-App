from django.urls import path
from . import views
from .views import (PostListView,
					PostDetailView,
					PostCreateView,
					PostUpdateView,
					PostDeleteView,
					UserPostListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>/', UserPostListView.as_view(template_name='blog/user_post.html'), name='user-post'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/search/', views.search, name='blog-search'),
    path('about/', views.about, name='blog-about'),
]
