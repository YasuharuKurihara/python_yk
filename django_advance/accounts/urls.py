from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

urlpatterns = [
    path('accounts_create/', views.AccountCreateView.as_view(), name='accounts_create'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Login.as_view(), name='logout'),
    path('home/', login_required(views.Home.as_view()), name='home'),
]
