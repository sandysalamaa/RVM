from rest_framework import serializers
from .models import Deposit , RewardRule
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ["id", "material", "weight", "machine_id", "timestamp", "points_awarded"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Deposit.objects.create(user=user, **validated_data)

class RewardRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardRule
        fields = '__all__'

class UserSummarySerializer(serializers.Serializer):
    total_weight = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_points = serializers.IntegerField()
