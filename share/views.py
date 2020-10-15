from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all() #all data in database
    }
    return render(request, 'share/home.html', context)


def about(request):
    return render(request, 'share/about.html', {'title': 'About'})