from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BankViewSet, BranchViewSet, BranchesByBankViewSet

router = DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'branches', BranchViewSet)

router.register(r'banks/(?P<bank_id>[^/.]+)/branches', BranchesByBankViewSet, basename='bank-branches')

urlpatterns = [
    path('', include(router.urls)),
]
