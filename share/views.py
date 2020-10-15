from django.shortcuts import render

posts = [
    {
        'author': 'Jamie',
        'title': 'post1',
        'content': 'first post content',
        'date_posted': 'January 13, 2020'
    },
    {
        'author': 'JimBob',
        'title': 'post2',
        'content': 'second post content',
        'date_posted': 'January 17, 2021'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'share/home.html', context)


def about(request):
    return render(request, 'share/about.html', {'title': 'About'})