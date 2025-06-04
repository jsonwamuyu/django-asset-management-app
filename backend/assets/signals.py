from django.db.models.signals import post_save, pre_delete, post_delete, pre_save
from django.dispatch import receiver
from .models import AssetAssignment
from .utils import notify_user_asset_assignment

@receiver(post_save, sender=AssetAssignment)
def send_assignment_notification_signal(sender, instance, created, **kwargs):
    """
    Signal to send notification when an Assignment is created.
    This function is triggered after an AssetAssignment instance is saved.
    """
    if created:

        notify_user_asset_assignment(instance.assigned_to.email, instance.asset.name, instance.asset.serial_number)
