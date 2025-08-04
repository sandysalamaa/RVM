from django.urls import path  
from .views import *

urlpatterns = [
    path("deposit/", DepositView.as_view()),
    path("summary/", UserSummeryView.as_view()),
    path("admin/reward-rules/", RewardRuleAdminView.as_view()),
]