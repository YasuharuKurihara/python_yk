# Generated by Django 4.2.2 on 2023-06-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='年齢'),
        ),
    ]
