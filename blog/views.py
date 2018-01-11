from django.http import HttpResponse
from .models import Post,Category
from django.shortcuts import render,get_object_or_404
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView

# Create your views here.

# def index(request):
#     return HttpResponse("欢迎访问我的博客首页")

# def index(request):
#     return render(request,'blog/index.html',context={
#         'title':'我的博客首页',
#         'welcome':'欢迎访问我的博客首页'
#     })

# def index(request):
#     # post_list=Post.objects.all().order_by('-created_time')#在blog.models下的Post类里写入class Meta:函数排序
#     post_list = Post.objects.all()
#     return render(request,'blog/index.html',context={
#         'post_list':post_list
#     })
#以类视图实现index
class IndexViews(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.increase_views()
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                ])
    form=CommentForm()
    comment_list=post.comment_set.all()
    context={
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request,'blog/detail.html',context=context)

# def archives(request,year,month):
#     post_list=Post.objects.filter(created_time_year=year,
#                                   created_time_month=month)
#     return render(request,'blog/index.html',context={'post_list':post_list})

#注意注意！！！！！！！！！！！！！！！！！！！created_time__year/created_time__month
# def archives(request, year, month):
#     post_list = Post.objects.filter(created_time__year=year,
#                                     created_time__month=month
#                                     )
#     return render(request, 'blog/index.html', context={'post_list': post_list})
class ArchivesView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        year=self.kwargs.get('year')
        month=self.kwargs.get('month')
        return super(ArchivesView,self).get_queryset().filter(created_time__year=year,
                                    created_time__month=month)


# def category(request, pk):
#     # 记得在开始部分导入 Category 类
#     cate = get_object_or_404(Category, pk=pk)
#     post_list = Post.objects.filter(category=cate).order_by('-created_time')
#     return render(request, 'blog/index.html', context={'post_list': post_list})


# class CategoryView(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'
#     def get_queryset(self):
#         cate=get_object_or_404(Category,pk=self.kwargs.get('pk'))
#         return super(CategoryView,self).get_queryset().filter(category=cate)

class CategoryView(IndexViews):
    def get_queryset(self):
        cate=get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoryView,self).get_queryset().filter(category=cate)
