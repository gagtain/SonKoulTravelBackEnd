from typing import List

from django.db import models

from tour.models import TourAdd

STAR_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),

]

class CommentView(models.Model):
    stars = models.IntegerField(default=0, choices=STAR_CHOICES, verbose_name="Оценка тура")
    name = models.CharField(max_length=100)
    text = models.TextField(verbose_name="ваш отзыв")
    image = models.ImageField(upload_to="static/images", verbose_name="Изображение")
    image_two = models.ImageField(upload_to="static/images", verbose_name="Изображение 2(необязательно)", null=True, blank=True)
    image_three = models.ImageField(upload_to="static/images", verbose_name="Изображение 3(необязательно)", null=True, blank=True)
    image_four = models.ImageField(upload_to="static/images", verbose_name="Изображение 4(необязательно)", null=True, blank=True)
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name="выбрать тур")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_approved = models.BooleanField(default=False)
    at_moderation = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")

    def __str__(self):

        return f"Комментарий: {self.id} Рейтинг: звезд: {self.stars}"

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'

        ordering = ['-date']
