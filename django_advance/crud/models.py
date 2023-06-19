from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone


class Goods(models.Model):
    name = models.CharField('商品名', unique=True, max_length=10)
    management_code = models.CharField('管理コード', unique=True, max_length=20)
    # MaxValueValidator(1000000000) 商品の価格は、10億円までしか登録できない
    price = models.PositiveIntegerField('価格', validators=[MaxValueValidator(1000000000)])
    release_date = models.DateField('発売日', default=timezone.now)
    release_flag = models.BooleanField('発売済み', default=False)
    description = models.TextField('商品説明')
    # FileField→ファイルなんでもアップロードできるフィールド
    # ImageField→画像アップロード用のフィールド
    image = models.ImageField('商品画像', null=True, blank=True, upload_to='goods_images/')
    state_flag = models.BooleanField('運用状況', default=True)

    def __str__(self):
        return self.name
