from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'

# Post CRUD
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
 
class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=Post 

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model=Post 

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_list.html'
    model = Post
      
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

############################################
# Comments

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form=CommentForm()
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
        
    return render(request, 'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)