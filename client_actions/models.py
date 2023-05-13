from django.db import models
from rest_framework.reverse import reverse

from tour.models import TourAdd

choices = [
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

for i in range(1, 11):
    choices.append((i, str(i)))


class CommentStar(models.Model):
    stars = models.IntegerField(default=0, choices=choices, verbose_name="Оценка тура")

    def __str__(self):
        return str(self.stars)

    class Meta:
        verbose_name_plural = 'Оценки туров'
        verbose_name = 'Оценка туров'


class CommentName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Имя пользователя'


class CommentText(models.Model):
    text = models.TextField()

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name_plural = 'отзывы'
        verbose_name = 'Отзыв'


class CommentImage(models.Model):
    image = models.ImageField(upload_to="static/images", verbose_name="Изображение")
    image_two = models.ImageField(upload_to="static/images", verbose_name="Изображение 2", blank=True, null=True)
    image_three = models.ImageField(upload_to="static/images", verbose_name="Изображение 3", blank=True, null=True)
    image_four = models.ImageField(upload_to="static/images", verbose_name="Изображение 4", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Прикрепить изображения'
        verbose_name = 'Прикрепить изображение'

        ordering = ['-image']
        unique_together = ['image']


class ChooseTour(models.Model):
    tour = models.OneToOneField(TourAdd, verbose_name="выбрать тур", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Выбрать тур'
        verbose_name = 'Выбрать тур'
        ordering = ['-tour']
        unique_together = ['tour']

    def __str__(self):
        return self.tour.name


class CommentView(models.Model):
    stars = models.ForeignKey(CommentStar, on_delete=models.CASCADE, verbose_name="Оценка тура(1-10)")
    name = models.ForeignKey(CommentName, on_delete=models.CASCADE, verbose_name="Имя пользователя")
    text = models.ForeignKey(CommentText, on_delete=models.CASCADE, verbose_name="ваш отзыв")
    image = models.ForeignKey(CommentImage,
                              related_name="Изображение",
                              on_delete=models.CASCADE,
                              blank=False, null=False,
                              verbose_name="Изображение")
    image_two = models.ForeignKey(CommentImage, on_delete=models.CASCADE, verbose_name="Изображение 2(необязательно)", \
                                  related_name="image_two_related",
                                  blank=True, null=True)
    image_three = models.ForeignKey(CommentImage, on_delete=models.CASCADE, verbose_name="Изображение 3(необязательно)",
                                    related_name="image_three_related",
                                    blank=True, null=True)
    image_four = models.ForeignKey(CommentImage, on_delete=models.CASCADE, verbose_name="Изображение 4(необязательно)",
                                   related_name="image_four_related",
                                   blank=True, null=True)
    tour = models.ForeignKey(ChooseTour, on_delete=models.CASCADE, verbose_name="выбрать тур")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self) -> str:
        return self.stars + self.name + self.text + self.image + str(self.tour) + str(self.date)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'

        ordering = ['-date']
