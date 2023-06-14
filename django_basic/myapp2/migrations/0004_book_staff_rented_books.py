# Generated by Django 4.2.2 on 2023-06-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0003_department_staff_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='書籍名')),
                ('management_code', models.CharField(max_length=50, unique=True, verbose_name='管理番号')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='rented_books',
            field=models.ManyToManyField(to='myapp2.book', verbose_name='借りている本'),
        ),
    ]
