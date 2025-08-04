from .models import RewardRule

def calculate_reward(material:str , weight : float) -> int:
    try:
        rule = RewardRule.objects.get(material = material)
        points = int(rule.points_per_kg * weight)
    except RewardRule.DoesNotExist:
        return 0