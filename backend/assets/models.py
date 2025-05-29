from django.db import models

class Asset(models.Model):
    """Model representing an asset."""
    name = models.CharField(max_length=100, verbose_name="Asset Name", help_text="Enter the name of the asset"),
    description = models.TextField(verbose_name="Asset Description", help_text="Enter brief description of the asset"),
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At",help_text="The date and time when the asset was created")

    def __str__(self):
        """String representation of the Asset model."""
        return self.name
    class Meta:
        """Meta options for the Asset model."""
        verbose_name = "Asset"
        verbose_name_plural = "Assets"
        ordering = ['created_at']


