from django.db import models

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=255,blank=True)
    url=models.URLField(blank=True)
    text=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)

    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE)#注意书写格式‘’

    def __str__(self):#错误点：__str__写成了__init__
        return self.text[:20]#什么意思