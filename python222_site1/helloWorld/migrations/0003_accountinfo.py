# Generated by Django 5.1.4 on 2024-12-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0002_booktypeinfo_bookinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('account', models.FloatField()),
            ],
            options={
                'verbose_name': '用户账户信息',
                'db_table': 't_account',
            },
        ),
    ]
