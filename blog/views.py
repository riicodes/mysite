from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post


class PostList(ListView):
    queryset = Post.published.all()
    template_name = 'blog/post/list.html'
    context_object_name = 'posts'
    paginate_by = 1


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html',
                  {'post': post})
