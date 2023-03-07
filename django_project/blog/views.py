from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' #taking the contexts from the 
    ordering = ['-date_Posted'] #this changes the ordering of the posts (the lists being displayed) in our blog 
    paginate_by = 5 #this puts only two items on the page
    
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts' #taking the contexts from the 
    ordering = ['-date_Posted'] #this changes the ordering of the posts (the lists being displayed) in our blog 
    paginate_by = 5 #this puts only two items on the page

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#the mixins ensure that the user is logged in before they can make changes 
#and also ensure that the user is the one the post belongs to
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

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