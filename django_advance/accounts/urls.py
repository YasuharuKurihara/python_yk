from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('accounts_create/', views.AccountCreateView.as_view(), name='accounts_create'),
]
