
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
    class Meta:
        model = Branch
        fields = ['id', 'bank', 'name', 'code', 'address', 'phone']
