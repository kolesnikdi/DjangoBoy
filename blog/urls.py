from . import views
from django.urls import path



urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    # path('json/post/', ListPostView.as_view(), name='json_post_detail'), # Get all!
    # path('json/post/<int:pk>/', PostView.as_view(), name='json_post_detail'), # Get single!
]
