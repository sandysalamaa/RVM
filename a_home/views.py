from .serializers import DepositSerializer , RewardRuleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import RewardRule
from .tasks import process_deposit_async

class DepositView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self , request):
        serializer = DepositSerializer(data = request.data , context = {'request':request})
        serializer.is_valid(raise_exception=True)
        deposit = serializer.save()
        process_deposit_async.delay(deposit.id)
        return Response(DepositSerializer(deposit).data , status=status.HTTP_201_CREATED)
        
class UserSummeryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        user = request.user
        total_weight = sum([d.weight for d in user.desposits.all()])
        total_points = sum([d.points_awarded for d in user.desposits.all()])
        summery = {'total_weight':total_weight , 'total_points':total_points}
        return Response(summery)
    
class RewardRuleAdminView(APIView):
    permission_classes = [permissions.IsAdminUser]
    
    def get(self,request):
        rules = RewardRule.objects.all()
        return Response(RewardRuleSerializer(rules , many = True).data)
    
    def post(self,request):
        serializer = RewardRuleSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

        

