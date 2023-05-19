import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.core.cache import caches  # Заменили get_cache на caches

from .models import FormQuestion
from .serializers import FormQuestionSerializer


class FormQuestionViewSet(viewsets.ModelViewSet):
    queryset = FormQuestion.objects.all()
    serializer_class = FormQuestionSerializer


    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)

            # Отправка данных в телеграмм
            bot_token = '5964377497:AAEXxcJ745bQpNUpB2neHIjMMkf0IBF5mn4'
            chat_id = '860389338'
            message = f'Question main page: {serializer.data["question_text"]}\nContacts: {serializer.data["contact"]}\n created_at: {str(serializer.data["created_at"])}'
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
            requests.post(url)

            headers = self.get_success_headers(serializer.data)
            responce_201 = {
                "message": "Your request has been successfully submitted!  Manager will contact you soon.",
            }
            return Response(responce_201, status=status.HTTP_201_CREATED, headers=headers)
        except Exception:
            responce_400 = {
                "message": "Your request has not been successfully submitted!  Please try again later."
            }

            return Response(responce_400, status=status.HTTP_400_BAD_REQUEST)
