from django.urls import path, include
from . import views

def generate_model_urls(prefix, view_module):
    """Generate standard CRUD URLs for a model"""
    return [
        path('', getattr(view_module, f'{prefix}_list'), name=f'{prefix}_list'),
        path('<int:pk>/', getattr(view_module, f'{prefix}_detail'), name=f'{prefix}_detail'),
        path('new/', getattr(view_module, f'{prefix}_create_or_update'), name=f'{prefix}_create'),
        path('<int:pk>/edit/', getattr(view_module, f'{prefix}_create_or_update'), name=f'{prefix}_update'),
        # This line includes the delete URL
        path('<int:pk>/delete/', getattr(view_module, f'{prefix}_delete'), name=f'{prefix}_delete'),
    ]

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', include(generate_model_urls('category', views))),
    path('budgets/', include(generate_model_urls('budget', views))),
    path('expenses/', include(generate_model_urls('expense', views))),
]

# AJAX API endpoints
api_urlpatterns = [
    path('api/categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('api/budgets/<int:pk>/delete/', views.budget_delete, name='budget_delete'),
    path('api/expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
]

urlpatterns += api_urlpatterns

# Update expenses/urls.py to include API endpoints
# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from . import views, api_views

# # Create a router for API views
# router = DefaultRouter()
# router.register(r'api/categories', api_views.CategoryViewSet, basename='category-api')
# router.register(r'api/budgets', api_views.BudgetViewSet, basename='budget-api')
# router.register(r'api/expenses', api_views.ExpenseViewSet, basename='expense-api')

# # Update urlpatterns
# urlpatterns = [
#     # Existing URL patterns
#     path('', views.dashboard, name='dashboard'),
#     path('categories/', include(generate_model_urls('category', views))),
#     path('budgets/', include(generate_model_urls('budget', views))),
#     path('expenses/', include(generate_model_urls('expense', views))),
    
#     # Add API URLs
#     path('', include(router.urls)),
# ]