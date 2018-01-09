from django import template
from ..models import Post

register=template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]