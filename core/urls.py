from django.urls import path
from rest_framework.routers import DefaultRouter
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import UserViewSet, CustomObtainTokenPairView

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet)

urlpatterns = [
    path("token/request/", CustomObtainTokenPairView.as_view(), name="token_request"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), 
]
urlpatterns += user_router.urls