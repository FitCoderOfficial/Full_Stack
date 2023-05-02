from django.urls import path, include
from .views import * 

urlpatterns = [
    path('v-like/<int:postId>/', VideoLikeView.as_view(), name="v-like"),
    path('sv-like/<int:postId>/', ShortVideoLikeView.as_view(), name="sv-like"),

    path('rm-v-like/<int:postId>/', VideoRemoveLikeView.as_view(), name="rm-v-like"),
    path('rm-sv-like/<int:postId>/', ShortVideoRemoveLikeView.as_view(), name="rm-sv-like"),

    path('v-dislike"/<int:postId>/', VideoDislikeView.as_view(), name="v-dislike"),
    path('sv-dislike/<int:postId>/', ShortVideoDislikeView.as_view(), name="sv-dislike"),

    path('rm-v-dislike/<int:postId>/', VideoRemoveDislikeView.as_view(), name="rm-v-dislike"),
    path('rm-sv-dislike/<int:postId>/', ShortVideoRemoveDislikeView.as_view(), name="rm-sv-dislike"),

]
