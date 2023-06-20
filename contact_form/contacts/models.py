from django.db import models


class BaseContact(models.Model):
    """抽象モデル 継承して使うためのクラス"""
    datetime = models.DateTimeField(verbose_name='お問合せ日時', auto_now_add=True)
    content = models.TextField(verbose_name='お問合せ内容', blank=False)
    email = models.EmailField(verbose_name='メールアドレス', blank=False)

    class Meta:
        # これがあると、テーブルが作られない
        abstract = True

    def __str__(self):
        return self.content


class IndividualContact(BaseContact):
    """個人からのお問合せ"""
    fullname = models.CharField(verbose_name='氏名', blank=False, max_length=30)
    kana = models.CharField(verbose_name='フリガナ', blank=False, max_length=60)


class CorporateContact(BaseContact):
    """企業からのお問合せ"""
    corporate_name = models.CharField(verbose_name='企業名', blank=False, max_length=30)
    pic_name = models.CharField(verbose_name='担当者名', blank=False, max_length=30)
    phonenumber = models.CharField(verbose_name='電話番号', blank=False, max_length=16)







