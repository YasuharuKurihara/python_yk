from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

#もともとあるUserCreationFormを継承する
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'is_active', 'age')