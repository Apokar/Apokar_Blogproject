from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse


# Create your models here.

@python_2_unicode_compatible
class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


@python_2_unicode_compatible
class Tag(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)


@python_2_unicode_compatible
class Post(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    title = models.CharField(max_length=90)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category)

    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    # 新增 views 字段记录阅读量
    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time', 'title']
