from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, BasePermission, IsAuthenticated
from middleware.custom_middleware import CustomAuthenticationMiddleware


@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_view(request):
    if request.user.is_superuser:
        return CustomAuthenticationMiddleware.call(request=request.user)
    else:
        return CustomAuthenticationMiddleware.call(request=request.user)


class IsUserAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
