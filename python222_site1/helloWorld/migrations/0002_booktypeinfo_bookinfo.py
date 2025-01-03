# Generated by Django 5.1.4 on 2024-12-24 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloWorld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTypeInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookTypeName', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': '图书类别信息',
                'db_table': 't_bookType',
            },
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bookName', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('publishDate', models.DateField()),
                ('bookType', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='helloWorld.booktypeinfo')),
            ],
            options={
                'verbose_name': '图书信息',
                'db_table': 't_book',
            },
        ),
    ]
