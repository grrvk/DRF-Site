from rest_framework.routers import DefaultRouter
from transport.viewsets import TransportViewSet

router = DefaultRouter()
router.register('transport', TransportViewSet, basename='transport2')

urlpatterns = router.urls