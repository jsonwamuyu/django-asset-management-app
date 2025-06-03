from rest_framework import viewsets, permissions
from .models import Asset, AssetAssignment, User
from .serializers import AssetSerializer, AssetAssignmentSerializer,UserSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrAssignedOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class AssetViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Asset model. Admin has full access, can create, update, delete, and list assets.
    """

    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]


class AssetAssignmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for assigning assets to users.
    - Admin can assign, view all.
    - Staff can view only their assigned assets.
    """

    queryset = AssetAssignment.objects.all()
    serializer_class = AssetAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrAssignedOnly]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return AssetAssignment.objects.all()
        elif user.role == 'staff':
            return AssetAssignment.objects.filter(assigned_to=user)
        return AssetAssignment.objects.none()

