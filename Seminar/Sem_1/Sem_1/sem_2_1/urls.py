from django.urls import path
from sem_2_1.views import get_post, post_full

urlpatterns = [
    path('posts/<int:author_id>/', get_post),
    path('post/<int:post_id', post_full)
]