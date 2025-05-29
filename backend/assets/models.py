from django.db import models
from django.contrib.auth.models import AbstractUser


# Extend the default User model using AbstractUser so we can distinguish between Admins and Staff
class User(AbstractUser):
    """Custom User model extending Django's AbstractUser."""
    is_admin = models.BooleanField(default=False, verbose_name="Is Admin", help_text="Designates whether the user can perform admin tasks.")
    """Boolean field to indicate if the user is an admin."""
    is_staff = models.BooleanField(default=True, verbose_name="Is Staff") # Default is a staff member
    """Boolean field to indicate if the user is a staff member."""

    def __str__(self):
        """String representing User model"""
        return self.username

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
    """Model representing and asset assignment."""
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True, verbose_name="Assigned At", help_text="The date and time when the asset was assigned")

    
    def __str__(self):
        return super().__str__()

    class Meta:
        ordering = ['asset']
        verbose_name = "Asset Assignment"
        verbose_name_plural = "Asset Assignments"



