from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' #taking the contexts from the 
    ordering = ['-date_Posted'] #this changes the ordering of the posts (the lists being displayed) in our blog 


class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

















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