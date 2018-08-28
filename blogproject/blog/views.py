from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.http import HttpResponse

import markdown
from comments.forms import CommentForm



# Create your views here.

# def index(request):
#    return render(request,'blog/index.html',context={
#            "title":'my blog',
#            "welcome":"welcome to apokar's blog~!"
#        })

def index(request):
    # post_list = Post.objects.all().order_by('-created_time')
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown 模块

    # 阅读量 +1
    post.increase_views()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)
