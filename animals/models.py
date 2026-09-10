from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# 1. 先定义 Category，因为 Animal 需要引用它
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories" # 优化后台显示名称

# 2. 定义唯一的 Animal 模型 (合并了你原本分散的两个定义)
class Animal(models.Model):
    name = models.CharField(max_length=100)
    # 关联分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="类别")
    image = models.ImageField(upload_to='animals/', null=True, blank=True, verbose_name="图片")
    description = models.TextField(verbose_name="描述")
    # 关联发布者 (建议使用 settings.AUTH_USER_MODEL 以支持自定义用户模型)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="发布者")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Animals"

# 3. 最后定义 Comment 和 Like，因为它们依赖上面的 Animal
class Comment(models.Model):
    # 使用字符串 'Animal' 引用，防止因加载顺序导致的潜在问题
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, related_name='comments', verbose_name="所属动物")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, verbose_name="评论者")
    content = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Comments"

    def __str__(self):
        username = self.user.username if self.user else "Anonymous"
        return f'Comment by {username} on {self.animal.name}'

class Like(models.Model):
    animal = models.ForeignKey('Animal', on_delete=models.CASCADE, related_name='likes', verbose_name="所属动物")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="点赞者")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="点赞时间")

    class Meta:
        unique_together = ('animal', 'user') # 防止同一个人重复点赞
        verbose_name_plural = "Likes"

    def __str__(self):
        return f'{self.user.username} likes {self.animal.name}'