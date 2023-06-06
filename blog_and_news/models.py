from django.db import models


class BlogNews(models.Model):
    title = models.CharField(max_length=100)
    CATEGORY_CHOICES = (
        ('News', 'News'),
        ('Blog', 'Blog'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images')
    content = models.TextField(verbose_name="Контент")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Добавить посты или новости'
        verbose_name = 'Добавить пост или новость'
