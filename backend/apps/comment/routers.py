from rest_framework.routers import DefaultRouter
from .views import CommentViewSet, ShortCommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'short_comments', ShortCommentViewSet, basename='short_comment')
urlpatterns = router.urls