from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.db.models import Q
from .pagination import CustomPagination


def staff_required(view_func):
    def wrapped_view(view_instance, request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(view_instance, request, *args, **kwargs)
        else:
            return Response({"message" : "You are not authorized"}, status=status.HTTP_401_UNAUTHORIZED)
    return wrapped_view



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.get_serializer().Meta.model.objects.filter(is_active=True)
            return self.queryset
        else:
            return self.queryset

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)
    
    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        else:
            return super().get_permissions()

    def list(self, request):
        user_serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = UserCreateSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def update(self, request, pk=None):
        user = self.get_object(pk=pk)
        user_serializer = self.serializer_class(user, data=request.data)
        # 이미지 데이터가 없거나 비어 있는 경우, 기존 이미지를 유지
        if 'image' not in request.data or request.data['image'] == "":
            request.data._mutable = True
            request.data['image'] = user.image
            request.data._mutable = False
            
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({"message" : "User updated successfully", 'data': user_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        user = self.serializer_class.Meta.model.objects.filter(is_active=True,pk=pk).first()
        if user:
            user_serializer = self.serializer_class(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message" : "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    @staff_required
    def destroy(self, request, pk=None):
        user = self.get_object(pk=pk)
        user.is_active = False
        if user.is_active == False:
            user.save()
            return Response({"message" : "User deleted successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message" : "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
    @action( methods=["POST"], detail=True)
    def change_password(self, request, pk=None):
        user = self.get_object(pk=pk)
        password_serializer = ChangePasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(request.data["password1"])
            user.save()
            return Response({"message" : "Password updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(password_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# AUTH
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(username=username, password=password)

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = UserLoggedSerializer(user)
                return Response({
                    "access": login_serializer.validated_data['access'],
                    "refresh": login_serializer.validated_data['refresh'],
                    "user": UserSerializer(user).data,
                    "message": "User logged in successfully",
                    }, status=status.HTTP_200_OK)
            else: 
                return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message" : "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
            

class SearchUserView(APIView):
    def get(self, request):
        search_term = request.query_params.get("search")
        matches = User.objects.filter(
            Q(username__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term)
        ).distinct()

        paginator = CustomPagination()
        results = paginator.paginate_queryset(matches, request)

        user_search_serializer = SearchUserSerializer(results, many=True)
        return paginator.get_paginated_response(user_search_serializer.data)

class UserLoggedDataView(APIView):
   def get(self, request):
       user = request.user
       user_serializer = UserLoggedSerializer(user)
       return Response(user_serializer.data, status=status.HTTP_200_OK)   
   
