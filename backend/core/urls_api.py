from rest_framework.routers import DefaultRouter
from .views_api import SignViewSet

router = DefaultRouter()
router.register(r'signs', SignViewSet)

urlpatterns = router.urls
