from django.http import JsonResponse


def upload_image(request, *args, **kwargs):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES.get('file')
        return JsonResponse({'url': '/app/media/' + file.name})
