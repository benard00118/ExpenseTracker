# expenses/models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_categories')  # Updated related_name

    def __str__(self):
        return self.name

class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_budgets')  # Updated related_name

    def __str__(self):
        return f"Budget for {self.user.username}: {self.amount}"

class Expense(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
        ('paypal', 'PayPal'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses_expenses')  # Updated related_name
    currency = models.CharField(max_length=10, default='USD')  # Field for currency
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='cash')  # New field for payment method
    tags = models.CharField(max_length=255, blank=True, null=True)  # Optional tags field

    def __str__(self):
        return f"{self.description} - {self.amount} {self.currency} ({self.payment_method})"