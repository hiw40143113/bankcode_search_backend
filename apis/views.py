from rest_framework import viewsets
from rest_framework.response import Response
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchesByBankViewSet(viewsets.ViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def list(self, request, bank_id=None):
        branches = self.queryset.filter(bank_id=bank_id)
        serializer = self.serializer_class(branches, many=True)
        return Response(serializer.data)
