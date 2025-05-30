from rest_framework import serializers
from .models import Asset , AssetAssignment, User



from django.contrib.auth import get_user_model

User =get_user_model()

class UserSerializer(serializers.Serializer):
    """Serializer for custom user model."""
    class Meta:
        """Meta class for UserSerializer."""
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']
        read_only_fields = ['id', 'username', 'email']
        ordering = ['username']


class AssetSerializer(serializers.ModelSerializer):
    """Serializer for Asset model."""

    class Meta:
        model = Asset
        fields = ['id', 'name', 'description', 'serial_number', 'created_at']
        read_only_fields = ['id', 'created_at']
        ordering = ['created_at']

class AssetAssignmentSerializer(serializers.ModelSerializer):
    """Serializer for AssetAssignment model."""

    asset = AssetSerializer(read_only=True)
    asset_id = serializers.PrimaryKeyRelatedField(
        queryset =Asset.objects.all(),
        write_only=True,
        source='asset'
    )

    assigned_to = UserSerializer(read_only=True)
    assigned_to_id=serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source='assigned_to'
    )
    
    class Meta:
        model = AssetAssignment
        fields = ['id', 'asset', 'assigned_at', 'assigned_to','asset_id','assigned_to_id' ]
        read_only_fields = ['id', 'assigned_at']
        ordering = ['assigned_at']