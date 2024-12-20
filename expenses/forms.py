from django import forms
from .models import Budget
from django import forms
from .models import Category, Budget, Expense

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'start_date', 'end_date']
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'date-input-container'}),  
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'date-input-container'
            }),
            'end_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'date-input-container'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['class'] = 'date-input-container'
        self.fields['end_date'].widget.attrs['class'] = 'date-input-container'
        
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'description', 'category']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'date-input-container'
            }),
            'category': forms.RadioSelect(attrs={'class': 'category-bubbles'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'date-input-container'
        
   