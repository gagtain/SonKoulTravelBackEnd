from django.http import JsonResponse
from rest_framework.exceptions import AuthenticationFailed


def process_exception(request, exception):
    if isinstance(exception, AuthenticationFailed):
        return JsonResponse({'error': 'Custom authentication error message'}, status=401)


class CustomAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
