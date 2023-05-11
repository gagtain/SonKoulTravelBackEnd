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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Добавить посты или новости'
        verbose_name = 'Добавить пост или новость'


class Body(models.Model):
    description = models.TextField()
    title_2 = models.CharField(max_length=255)
    quote = models.CharField(max_length=255, blank=True, null=True)
    description_2 = models.TextField()
    image = models.ImageField(upload_to='blog_images')
    image_2 = models.ImageField(upload_to='blog_images')
    image_3 = models.ImageField(upload_to='blog_images')
    title_3 = models.CharField(max_length=255)
    description_3 = models.TextField()
    title_4 = models.CharField(max_length=100)
    description_4 = models.TextField()
    title_5 = models.CharField(max_length=100)
    description_5 = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Добавить контент к постам или к новостям'
        verbose_name = 'Добавить контент к посту или к новости'
