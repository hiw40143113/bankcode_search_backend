from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BankViewSet, BranchViewSet

router = DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'branches', BranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
