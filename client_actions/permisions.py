from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from middleware.custom_middleware import CustomAuthenticationMiddleware


@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_view(request):
    user = request.user
    if user.is_superuser:
        return CustomAuthenticationMiddleware.__call__(request=request.user)
    return CustomAuthenticationMiddleware.__call__(request=request.user)
