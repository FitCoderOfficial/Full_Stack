from django.urls import path, include
from .views import * 


urlpatterns = [
    path('users-search/', SearchUserView.as_view(), name='users-search'),
    path('users-logged/', UserLoggedDataView.as_view(), name='users-logged')
]
