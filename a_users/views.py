from a_users.serializers import UserLoginSerializer , UserRegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    def post(self,request):
        serializer = UserRegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user) #Refresh token
        return Response({'refresh':str(token) , 'access':str(token.access_token)})

class LoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data = request.data , context = {'request':request}) 
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = RefreshToken.for_user(user)
        return Response({"refresh": str(token), "access": str(token.access_token)})