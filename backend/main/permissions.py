from rest_framework.permissions import BasePermission, SAFE_METHODS

from django.contrib.auth.models import User

from re import findall


class IsOwner(BasePermission):
    """
    Permiso personal para sólo propietarios del objeto a editar
    """
    
    def has_permission(self, request, view):
        pk = findall('[0-9]', request.path)[0]

        user = User.objects.get(consumer=pk)
        
        if user == request.user:
            return True

        return False