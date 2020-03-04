from rest_framework import routers
from .api import EventViewSet

router = routers.DefaultRouter()
router.register('list', EventViewSet, 'events')

urlpatterns = router.urls