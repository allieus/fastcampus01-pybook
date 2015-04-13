# coding: utf8
from os.path import abspath  # noqa
from django.shortcuts import get_object_or_404, redirect, render
from blog.forms import PostForm
from blog.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {
        'posts': posts,
    })


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def new(request, id=None):
    if id is not None:
        post = get_object_or_404(Post, id=id)
    else:
        post = None

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def edit(request, id):
    return new(request, id)


def delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return render(request, 'blog/post_confirm_delete.html', {
    })
