from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #UserモデルにもともとあるがユニークにしたいのでEmailフィールドを上書き
    email = models.EmailField('メールアドレス', unique=True)

    #Userモデルにないフィールドの追加
    age = models.PositiveIntegerField('年齢', default=0)
