from django.shortcuts import render
from .models import Post  # .models means look in current package


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = { 'title' : 'blog-about'}
    return render(request, 'blog/about.html', context)