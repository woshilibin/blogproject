from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    title="博客学习"
    link="/"
    description="博客项目学习"
    def items(self):
        return Post.objects.all()
    def item_title(self, item):
        return '[%s] %s' % (item.category,item.title)
    def item_description(self, item):
        return item.body