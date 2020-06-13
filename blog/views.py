from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, CreateView, ListView, DeleteView, DetailView, UpdateView)
from blog.models import Post, Comments
from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

class AboutView(TemplateView):
    template_name = 'blog/about.html'


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    form_class = PostForm


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail'
    form_class = PostForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    mdoel = Post
    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = '/login'
    redirect_field_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

@login_required
def add_comments_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comments, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)