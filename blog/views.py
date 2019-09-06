from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post  # .models means look in current package


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    """
    Lists all posts
    - By default, looks for templates of a certain naming convention
      i.e. <app>/<model>_<viewtype>.html
    - Calls the object 'object_list' by default - we can change that in template OR below
    """
    model = Post
    template_name = 'blog/home.html'    # Replaces default template name
    context_object_name = 'posts'       # Replaces default object name
    ordering = ['-date_posted']         # '-' orders from newest to oldest
    paginate_by = 5                     # Posts per page


class UserPostListView(ListView):
    """
    Lists all posts
    - By default, looks for templates of a certain naming convention
      i.e. <app>/<model>_<viewtype>.html
    - Calls the object 'object_list' by default - we can change that in template OR below
    """
    model = Post
    template_name = 'blog/user_posts.html'  # Replaces default template name
    context_object_name = 'posts'           # Replaces default object name
    paginate_by = 5                         # Posts per page

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """
    Shows details of a single post
    Looks for 'blog/post_detail.html'
    """
    model = Post


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        """ Prevent users from deleting other peoples post """
        post = self.get_object()
        return self.request.user == post.author


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Shows creation page for a post
    Looks for 'blog/post_form.html'
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Prevent users from updating other peoples post """
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    context = { 'title' : 'blog-about'}
    return render(request, 'blog/about.html', context)
