from django.db import models


class FormQuestion(models.Model):
    question_text = models.TextField(verbose_name="Write your question")
    contact = models.CharField(verbose_name="Leave your E-mail or WhatsApp", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)