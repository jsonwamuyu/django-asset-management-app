from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AssetViewSet, AssetAssignmentViewSet, UserViewSet
from . import views

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r'assets', AssetViewSet, basename='asset')
router.register(r'asset-assignments', AssetAssignmentViewSet, basename='assignment')

# URL patterns for the assets app
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]