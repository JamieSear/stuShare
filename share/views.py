from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all() #puts all data in db
    }
    return render(request, 'share/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'share/home.html'  # looking for template in share/post_detail.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4


class UserListView(ListView): #see other user's profiles and posts
    model = Post
    template_name = 'share/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #either gets user or sends 404
        return Post.objects.filter(author=user).order_by('-date_posted') #orders by date posted again


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user # Sets author of form
        return super().form_valid(form) #validates form on parent class with author

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author: #checks if user is the author!
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' #redirects to home once deleted

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'share/about.html', {'title': 'About'})