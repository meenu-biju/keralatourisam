# Generated by Django 3.2.7 on 2021-10-09 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourisamapp', '0003_alter_news_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='check',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
    ]
