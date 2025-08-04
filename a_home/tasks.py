from celery import shared_task
from .models import Deposit
from .reward_engine import calculate_reward

@shared_task
def process_deposit_async(deposit_id):
    try:
        deposit = Deposit.objects.get(id = deposit_id)
        points = calculate_reward(deposit.material , float(deposit.weight))
        deposit.points_awarded = points
        deposit.save()
    except Deposit.DoesNotExist:
        pass