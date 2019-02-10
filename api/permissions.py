from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = 'blah you cant do that'
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.owner == request.user):
            return True
        else:
            return False
