import logging

logger = logging.getLogger(__name__)

class RequestLoggingAndSecurityMiddleware:


    def __init__(self, get_response):
        self.get_response = get_response
        logger.info("RequestLoggingAndSecurityMiddleware initialized.")

    def __call__(self, request):
        # Code to execute for each request before the view (and later middleware) are called.
        logger.info(f"Request received: {request.method} {request.get_full_path()} from {self._get_client_ip(request)}")

        # Call the next middleware or view
        response = self._get_response(request)

        # Code to execute for each response after the view is called.

        # Add security headers to the response
        response['X-Frame-Options'] = 'DENY'  # Prevent clickjacking
        response['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'  # Enforce HTTPS
        response['Content-Security-Policy'] = "default-src 'self'"  # Restrict resource loading

        return response
    

    def _get_client_ip(self, request):
        """
        Get the clients's IP address from the request."""

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip