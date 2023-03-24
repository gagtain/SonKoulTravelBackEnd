from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, BasePermission, IsUserAuthor
from middleware.custom_middleware import CustomAuthenticationMiddleware


@api_view(['GET'])
@permission_classes([IsAdminUser])
def admin_view(request):
    user = request.user
    if user.is_superuser:
        return CustomAuthenticationMiddleware.__call__(request=request.user)
    return CustomAuthenticationMiddleware.__call__(request=request.user)


@permission_classes([IsUserAuthor])
class IsUserAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_author:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin:
            return True
        return False
