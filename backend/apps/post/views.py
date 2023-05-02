from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.user.pagination import CustomPagination
from rest_framework.views import APIView



def is_owner(request, instance):
    return request.user == instance.uploader or request.user.is_staff


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = Video.objects.all()
            return self.queryset
        else:
            return self.queryset
        
    def get_object(self, pk=None):
        return get_object_or_404(Video, pk=pk)
        
    def list(self, request):
        videos = self.serializer_class.Meta.model.objects.order_by('-id')
        paginator = CustomPagination()
        results = paginator.paginate_queryset(videos, request)

        posts_serializer = self.serializer(results, many=True)
        return paginator.get_paginated_response(posts_serializer.data)
        
    def create(self, request):
        video_serializer = VideoCreateSerializer(data=request.data)
        if video_serializer.is_valid():
            video_serializer.save(uploader=request.user)
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        videos = self.get_object(pk=pk)
        video_serializer = self.serializer_class(videos)
        return Response(video_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        video = self.get_object(pk)
        if not is_owner(request, video):
            return Response({"error": "You can't edit this video."}, status=status.HTTP_403_FORBIDDEN)
        else:
            if "video_url" in request.data or request.data['video_url'] == "":
                data = request.data.copy()
                data['video_url'] = video.video_url

                video_serializer = VideoCreateSerializer(video, data=data)
                if video_serializer.is_valid():
                    video_serializer.save()
                    return Response(video_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                video_serializer = VideoCreateSerializer(video, data=request.data)
                if video_serializer.is_valid():
                    video_serializer.save()
                    return Response({'message':'Post updated successfully', 'data': video_serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
    def destroy(self, request, pk=None):
        video = self.get_object(pk)
        if not is_owner(request, video):
            return Response({"error": "You can't delete this video."}, status=status.HTTP_403_FORBIDDEN)
        else:
            video.delete()
            return Response({"message": "Video deleted successfully."}, status=status.HTTP_200_OK)
        

class VideoLikeView(APIView):
    def post(self, request, video_id):
        try:
            # post.likes += 1
            video = get_object_or_404(Video, pk=video_id)
            video.likes.add(request.user)
            return Response({"message": "Video liked successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)

class VideoRemoveLikeView(APIView):
    def delete(self, request, video_id):
        try:
            video = get_object_or_404(Video, pk=video_id)
            video.likes.remove(request.user)
            return Response({"message": "Video like removed successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)

class VideoDislikeView(APIView):
    def post(self, request, video_id):
        try:
            video = get_object_or_404(Video, pk=video_id)
            video.dislikes.add(request.user)
            return Response({"message": "Video disliked successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)
        
class VideoRemoveDislikeView(APIView):
    def delete(self, request, video_id):
        try:
            video = get_object_or_404(Video, pk=video_id)
            video.dislikes.remove(request.user)
            return Response({"message": "Video dislike removed successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "Video not found."}, status=status.HTTP_404_NOT_FOUND)



# ShortVideo ViewSet 


class ShortVideoViewSet(viewsets.ModelViewSet):
    serializer_class = ShortVideoSerializer

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = ShortVideo.objects.all()
            return self.queryset
        else:
            return self.queryset
        
    def get_object(self, pk=None):
        return get_object_or_404(ShortVideo, pk=pk)
        
    def list(self, request):
        shortvideos = self.serializer_class.Meta.model.objects.order_by('-id')
        paginator = CustomPagination()
        results = paginator.paginate_queryset(shortvideos, request)

        posts_serializer = self.serializer(results, many=True)
        return paginator.get_paginated_response(posts_serializer.data)
        
    def create(self, request):
        shortvideo_serializer = ShortVideoCreateSerializer(data=request.data)
        if shortvideo_serializer.is_valid():
            shortvideo_serializer.save(uploader=request.user)
            return Response(shortvideo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(shortvideo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        shortvideos = self.get_object(pk=pk)
        shortvideo_serializer = self.serializer_class(shortvideos)
        return Response(shortvideo_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        shortvideo = self.get_object(pk)
        if not is_owner(request, shortvideo):
            return Response({"error": "You can't edit this shortvideo."}, status=status.HTTP_403_FORBIDDEN)
        else:
            if "video_url" in request.data or request.data['video_url'] == "":
                data = request.data.copy()
                data['video_url'] = shortvideo.shortvideo_url

                shortvideo_serializer = ShortVideoCreateSerializer(shortvideo, data=data)
                if shortvideo_serializer.is_valid():
                    shortvideo_serializer.save()
                    return Response(shortvideo_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(shortvideo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                shortvideo_serializer = ShortVideoCreateSerializer(shortvideo, data=request.data)
                if shortvideo_serializer.is_valid():
                    shortvideo_serializer.save()
                    return Response({'message':'Post updated successfully', 'data': shortvideo_serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response(shortvideo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
    def destroy(self, request, pk=None):
        shortvideo = self.get_object(pk)
        if not is_owner(request, shortvideo):
            return Response({"error": "You can't delete this shortvideo."}, status=status.HTTP_403_FORBIDDEN)
        else:
            shortvideo.delete()
            return Response({"message": "ShortVideo deleted successfully."}, status=status.HTTP_200_OK)
        

class ShortVideoLikeView(APIView):
    def post(self, request, video_id):
        try:
            # post.likes += 1
            shortvideo = get_object_or_404(ShortVideo, pk=video_id)
            shortvideo.likes.add(request.user)
            return Response({"message": "ShortVideo liked successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "ShortVideo not found."}, status=status.HTTP_404_NOT_FOUND)

class ShortVideoRemoveLikeView(APIView):
    def delete(self, request, video_id):
        try:
            shortvideo = get_object_or_404(ShortVideo, pk=video_id)
            shortvideo.likes.remove(request.user)
            return Response({"message": "Short Video like removed successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "Short Video not found."}, status=status.HTTP_404_NOT_FOUND)

class ShortVideoDislikeView(APIView):
    def post(self, request, video_id):
        try:
            shortvideo = get_object_or_404(ShortVideo, pk=video_id)
            shortvideo.dislikes.add(request.user)
            return Response({"message": "Short Video disliked successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "Short Video not found."}, status=status.HTTP_404_NOT_FOUND)
        
class ShortVideoRemoveDislikeView(APIView):
    def delete(self, request, video_id):
        try:
            shortvideo = get_object_or_404(ShortVideo, pk=video_id)
            shortvideo.dislikes.remove(request.user)
            return Response({"message": "Short Video dislike removed successfully."}, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({"error": "Short Video not found."}, status=status.HTTP_404_NOT_FOUND)