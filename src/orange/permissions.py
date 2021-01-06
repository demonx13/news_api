from rest_framework import permissions

class PublicPermissions(permissions.BasePermission):
    """Public permissions to view articles
    """

    def get_permissions(self):
        """
        set permission AllowAny for get/list request
        :return: [permission]
        """
        if self.actions == 'get' or self.actions == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
