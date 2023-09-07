from django.shortcuts import render, get_object_or_404
from sem_2_1.models  import Author, Post

def get_post(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'sem_2_1/main.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'sem_2_1/post_full.html', {'post': post})

