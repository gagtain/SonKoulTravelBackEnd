import uuid

from django.db import models

from client_actions.fields import WEBPField


def image_folder(instance, filename):
    return 'photos/{}.webp'.format(uuid.uuid4().hex)


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


class CommentStar(models.Model):
    stars = models.IntegerField(default=0, choices=choices)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.stars) + ' ' + str(self.name)

    class Meta:
        verbose_name_plural = 'Comment Stars'
        verbose_name = 'Comment Star'


class CommentName(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Comment Names'
        verbose_name = 'Comment Name'


class CommentText(models.Model):
    text = models.TextField()

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name_plural = 'Comment Texts'
        verbose_name = 'Comment Text'


class CommentImage(models.Model):
    image = WEBPField(
        verbose_name='Image',
        upload_to=image_folder,
    )

    class Meta:
        verbose_name_plural = 'Comment Images'
        verbose_name = 'Comment Image'

        ordering = ['-image']
        unique_together = ['image']


class CommentView(models.Model):
    stars = models.ForeignKey(CommentStar, on_delete=models.CASCADE)
    name = models.ForeignKey(CommentName, on_delete=models.CASCADE)
    text = models.ForeignKey(CommentText, on_delete=models.CASCADE)
    image = models.ForeignKey(CommentImage, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stars + self.name + self.text + self.image + str(self.date)

    class Meta:
        verbose_name_plural = 'Comment Views'
        verbose_name = 'Comment View'

        ordering = ['-date']
        unique_together = ['name']


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = WEBPField(
        verbose_name='Image',
        upload_to=image_folder,
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + str(self.date)

    class Meta:
        verbose_name = 'Опубликовать пост'
        verbose_name_plural = 'Опубликовать посты'

        unique_together = ['id']


class FormQuestion(models.Model):
    question = models.CharField(max_length=100, verbose_name="ваш вопрос")
    contact = models.CharField(max_length=100, verbose_name="контакты")
    created = models.DateTimeField(auto_now_add=True)


