from django.urls import path, include
from .views import * 

urlpatterns = [
    path('v-like/<int:video_id>/', VideoLikeView.as_view(), name="v-like"),
    path('sv-like/<int:video_id>/', ShortVideoLikeView.as_view(), name="sv-like"),

    path('rm-v-like/<int:video_id>/', VideoRemoveLikeView.as_view(), name="rm-v-like"),
    path('rm-sv-like/<int:video_id>/', ShortVideoRemoveLikeView.as_view(), name="rm-sv-like"),

    path('v-dislike/<int:video_id>/', VideoDislikeView.as_view(), name="v-dislike"),
    path('sv-dislike/<int:video_id>/', ShortVideoDislikeView.as_view(), name="sv-dislike"),

    path('rm-v-dislike/<int:video_id>/', VideoRemoveDislikeView.as_view(), name="rm-v-dislike"),
    path('rm-sv-dislike/<int:video_id>/', ShortVideoRemoveDislikeView.as_view(), name="rm-sv-dislike"),

]
