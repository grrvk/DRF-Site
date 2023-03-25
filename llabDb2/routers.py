from rest_framework.routers import DefaultRouter
from transport.viewsets import TransportViewSet

router = DefaultRouter()
router.register('transports', TransportViewSet, basename='transports')

urlpatterns = router.urls