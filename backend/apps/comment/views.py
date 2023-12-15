from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class CommentViewSet(viewsets.ModelViewSet):
    """
    댓글을 위한 ViewSet. 기본적으로 모든 사용자가 댓글을 읽을 수 있지만,
    댓글을 생성, 수정, 삭제하기 위해서는 인증이 필요합니다.
    """
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """
        생성 및 수정 요청에는 CommentCreateSerializer를 사용하고,
        나머지 경우에는 CommentSerializer를 사용합니다.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        """
        댓글 생성 시, 현재 로그인한 사용자를 댓글 작성자로 설정합니다.
        """
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        댓글 생성 요청 처리. 유효성 검사 후 댓글을 저장하고, 성공 응답을 반환합니다.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            

    
class ShortCommentViewSet(viewsets.ModelViewSet):
    """
    댓글을 위한 ViewSet. 기본적으로 모든 사용자가 댓글을 읽을 수 있지만,
    댓글을 생성, 수정, 삭제하기 위해서는 인증이 필요합니다.
    """
    queryset = ShortComment.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """
        생성 및 수정 요청에는 CommentCreateSerializer를 사용하고,
        나머지 경우에는 CommentSerializer를 사용합니다.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return ShortCommentCreateSerializer
        return ShortCommentSerializer

    def perform_create(self, serializer):
        """
        댓글 생성 시, 현재 로그인한 사용자를 댓글 작성자로 설정합니다.
        """
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        댓글 생성 요청 처리. 유효성 검사 후 댓글을 저장하고, 성공 응답을 반환합니다.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

