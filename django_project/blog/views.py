from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# ====================================================================
# posts = [
#     {
#         'author':'Cisco Ramon',
#         'title': 'Steal Like An Artist',
#         'content': 'First post content',
#         'date_posted': '12-01-2023' 
#     },
#     {
#         'author':'Jordin Smoak',
#         'title': 'The Dilemma of a Percher',
#         'content': 'Second post content',
#         'date_posted': '12-09-2023' 
#     },
#     {
#         'author':'Shine Teye',
#         'title': 'Eat That Frog',
#         'content': 'Third post content, 21 ways ways to avoid procrastination',
#         'date_posted': '12-09-2023' 
#     },

# ]