import logging

logger = logging.getLogger(__name__)


class AssetManagementMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logger.info("AssetManagementMiddleware initialized.")

    def __call__(self, request):

        response = self.get_response(request)

        return response