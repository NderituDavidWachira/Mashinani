from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import User
from core.serializers import UserSerializer, CustomTokenObtainPairSerializer


class CustomObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)

    def create(self, request, *args, **kwargs):
        # Custom user creation with error handling
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'user': UserSerializer(user).data,
                    'message': 'User created successfully'
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
