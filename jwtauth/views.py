# import class yang dibutuhkan untuk membuat view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
# import class untuk autentikasi jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.views import TokenObtainPairView
# import model dan class seriallizers untuk semua modul
from django.contrib.auth.models import User
from .seriallizers import MyTokenObtainPairSerializer, RegisterSerializer, LogoutSerializer
from rest_framework.permissions import AllowAny


# Membuat view untuk API endpoint "Register"
# POST:/api/register/
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# Membuat View untuk memodifikasi ObtainTokenPairView menjadi API endpoint "Login"
# POST:/api/login/
class CustomLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['message'] = 'Login successful!'
        return response


    
# Membuat View untuk API endpoint "Logout" dan memblacklist token
# POST:/api/logout/
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
  
     
     
# Membuat View untuk API endpoint "Logout/all" dan memblacklist semua token pengguna yang terkait
# POST:/api/logout/all
class LogoutAllSessionsView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response({"message": "Successfully logged out from all sessions"}, status=status.HTTP_205_RESET_CONTENT)
