from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import PaymentListAPIView, UserCreateAPIView, UserListAPIView, UserDetailAPIView, UserUpdateAPIView, \
    UserDeleteAPIView

app_name = 'users'

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),

    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit/', UserUpdateAPIView.as_view(), name='user-edit'),
    path('users/<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),

]
