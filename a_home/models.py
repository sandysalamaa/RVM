from django.db import models
from a_users.models import User

class RewardRule(models.Model):
    MATERIAL_CHOICES = [
        ("plastic", "Plastic"),
        ("metal", "Metal"),
        ("glass", "Glass")
    ]
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, unique=True)
    points_per_kg = models.DecimalField(max_digits=5, decimal_places=2)

class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deposits")
    material = models.CharField(max_length=20)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    machine_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    points_awarded = models.IntegerField(default=0)