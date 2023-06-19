from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import MyUserCreationForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin


class AccountCreateView(generic.CreateView):
    Model = CustomUser
    # form_class = UserCreationForm  # ユーザー作成するための、提供されているフォーム
    form_class = MyUserCreationForm
    template_name = 'accounts/accounts_create.html'
    success_url = reverse_lazy('accounts:create')

class Login(LoginView):
    template_name = 'accounts/login.html'

class Logout(LogoutView):
    #ログアウト後に移動するページ
    next_page = reverse_lazy('accounts:login')

class Home(TemplateView):
    template_name = 'accounts/home.html'

#urlsではなくviewsでloginrequiredを使用する場合の記述
# class Home(LoginRequiredMixin, TemplateView):
#     template_name = 'accounts/home.html'