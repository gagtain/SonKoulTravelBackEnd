from django.db import models


class FormQuestion(models.Model):
    question_text = models.TextField(verbose_name="Write your question")
    contact = models.CharField(verbose_name="Leave your E-mail or WhatsApp", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class OurTeam(models.Model):
    image = models.ImageField(upload_to='our_team', verbose_name="Фото сотрудника")
    name = models.CharField(verbose_name="Имя", max_length=100)
    position = models.CharField(verbose_name="Должность", max_length=200)
    experience = models.CharField(verbose_name="Опыт", max_length=200, blank=True, null=True)
    quote = models.TextField(verbose_name="Цитата")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"
        db_table = 'our_team'



