import logging

logger = logging.getLogger(__name__)


class AssetManagementMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logger.info("AssetManagementMiddleware initialized.")

    def __call__(self, request):
        user = request.user
        path = request.path

        if user.is_authenticated:
            logger.info(f"User {user.username} Role: {user.role} accessed {path}")

        response = self.get_response(request)

        if user.is_authenticated:
            logging.info(f"Response sent to {user.username} for {path}")
            
        return response