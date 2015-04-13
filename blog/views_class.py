# coding: utf8
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from blog.forms import PostForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

index = PostListView.as_view()


detail = DetailView.as_view(
    model=Post,
    # template_name='blog/post_detail.html',
    pk_url_kwarg='id',
)


new = CreateView.as_view(
    model=Post,
    form_class=PostForm,
    pk_url_kwarg='id',
    # success_url=reverse_lazy('blog:index'),
)


edit = UpdateView.as_view(
    model=Post,
    form_class=PostForm,
    pk_url_kwarg='id',
    # success_url=reverse_lazy('blog:index'),
)

delete = DeleteView.as_view(
    model=Post,
    pk_url_kwarg='id',
    success_url=reverse_lazy('blog:index'),
)
