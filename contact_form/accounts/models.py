from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_received_email = models.BooleanField(verbose_name='お問い合わせメールを受け取るか', default=True)
