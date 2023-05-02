from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'videos', VideoViewSet, basename='videos')
router.register(r'short_videos', ShortVideoViewSet, basename='short_videos')
urlpatterns = router.urls