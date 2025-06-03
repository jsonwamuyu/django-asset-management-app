from django.db import models
from django.contrib.auth.models import AbstractUser



# Extend the default User model using AbstractUser so we can distinguish between Admins and Staff
class User(AbstractUser):
    """Custom User model extending Django's AbstractUser."""

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff', verbose_name="User Role", help_text="Select the role of the user")


    def __str__(self):
        """String representing User model"""
        return f'{self.username} ({self.get_role_display()})'
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['username']


class Asset(models.Model):
    """Model representing an asset."""
    name = models.CharField(max_length=100, verbose_name="Asset Name", help_text="Enter the name of the asset")
    description = models.TextField(verbose_name="Asset Description", help_text="Enter brief description of the asset")
    serial_number = models.CharField(max_length=50, unique=True, verbose_name="Serial Number", help_text="Enter the unique serial number of the asset")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At",help_text="The date and time when the asset was created")


    def __str__(self):
        """String representation of the Asset model."""
        return self.name

    class Meta:
        """Meta options for the Asset model."""
        verbose_name = "Asset"
        verbose_name_plural = "Assets"
        ordering = ['created_at']


class AssetAssignment(models.Model):
    """Model representing asset assignment."""
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True, verbose_name="Assigned At", help_text="The date and time when the asset was assigned")
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Assigned To", help_text="The user to whom the asset is assigned")

    
    def __str__(self):
        return f"{self.asset.name} assigned to {self.assigned_to.username}"

    class Meta:
        ordering = ['asset']
        verbose_name = "Asset Assignment"
        verbose_name_plural = "Asset Assignments"



