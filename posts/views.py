from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, CreateView, FormMixin, DeleteView
from .models import Post, Like, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from posts.mixins import  OwnerOnlyMixin
# Create your views here.

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['body', 'image']
    template_name='main/home.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostDetailView(DetailView):
    model = Post

class PostUpdateView(OwnerOnlyMixin,UpdateView):
    model=Post
    fields=['body']
    template_name='posts/update.html'
    success_url = reverse_lazy('home')
    owner = 'author'



class PostDeleteView(OwnerOnlyMixin,DeleteView):
    model=Post
    template_name='posts/delete.html'
    success_url = reverse_lazy('home')
    owner = 'author'

@login_required
def add_comments(request):
    if request.method == 'POST':
        body=request.POST.get('cmt_txt')
        id=request.POST.get('post_id')
        post=Post.objects.get(id=id)
        user=request.user
        new_comment=Comment.objects.create(body=body, author= user, post=post)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def add_remove_likes(request):
    profile= request.user
    if request.method == 'POST':
        post_id = request.POST.get('id')
        post = Post.objects.get (id = post_id)
        if profile in post.get_all_likers():
            like=Like.objects.filter(profile=profile, post=post)
            like.delete()
            like_btn = 'Up'

        else:
            Like.objects.create(profile=profile, post=post)
            like_btn = 'Down'

    total_likes = post.get_total_likes()
    data = {'total_likes': total_likes, 'id':post_id, 'like_btn': like_btn }
    return JsonResponse(data,safe=False)
