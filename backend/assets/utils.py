import logging

logger = logging.getLogger(__name__) # Will use the app name as the logger name

def notify_user_asset_assignment(user_email, asset_name, serial_number):
    """
    Sends an email notification to the user when an asset is assigned to them.
    Args:
        user_email (str): The email address of the user to notify.
        asset_name (str): The name of the asset assigned.
        serial_number (str, optional): The serial number of the asset. Defaults to None.
    """
    logger.info(f"Sending asset assignment notification to {user_email} for asset {asset_name} with serial number {serial_number}")

    if serial_number is None:
        serial_number = "N/A"   # Default value if serial number is not provided

    # Prepare the email content

    subject = "NEW ASSET ASSIGNMENT NOTIFICATION"
    message = f'Hello, \n\nASSET NAME: {asset_name}\nSERIAL NUMBER: ({serial_number}).\n\nPlease take good care of it.\n\nBest regards,\nAsset Management Team'
    from_email = None  # Use default email settings
    recipient_list = [user_email]
    try:
        from django.core.mail import send_mail
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"Success: Notification sent to {user_email} for asset {asset_name}, serial number: {serial_number}.")
    except Exception as e:
        logger.info(f"Failed to send email: {e}")