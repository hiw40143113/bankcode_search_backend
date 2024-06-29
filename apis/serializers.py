
from rest_framework import serializers
from .models import Bank, Branch

class BankSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Bank
        fields = ['id', 'name', 'code', 'display_name']

    def get_display_name(self, obj):
        return f"{obj.code} {obj.name}"


class BranchSerializer(serializers.ModelSerializer):
    bank_code = serializers.CharField(source='bank.code', read_only=True)
    bank_name = serializers.CharField(source='bank.name', read_only=True)

    class Meta:
        model = Branch
        fields = ['id', 'bank', 'name', 'code', 'address', 'phone', 'bank_code', 'bank_name']
