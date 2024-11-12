# expenses/serializers.py
from rest_framework import serializers
from .models import Category, Budget, Expense

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'user']
        read_only_fields = ['user']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'amount', 'start_date', 'end_date', 'user']
        read_only_fields = ['user']

class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'date', 'description', 'category', 'category_name', 'user']
        read_only_fields = ['user']