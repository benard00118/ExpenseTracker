
# expenses/api_views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, BudgetSerializer, ExpenseSerializer
from .models import Category, Budget, Expense
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from django.utils import timezone

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        total_expenses = self.get_queryset().aggregate(Sum("amount"))["amount__sum"] or 0
        monthly_expenses = (
            self.get_queryset()
            .filter(date__month=timezone.now().month)
            .aggregate(Sum("amount"))["amount__sum"] or 0
        )
        
        budget = Budget.objects.filter(user=request.user).last()
        budget_amount = budget.amount if budget else 0
        budget_remaining = budget_amount - monthly_expenses

        return Response({
            "total_expenses": total_expenses,
            "monthly_expenses": monthly_expenses,
            "budget_amount": budget_amount,
            "budget_remaining": budget_remaining
        })