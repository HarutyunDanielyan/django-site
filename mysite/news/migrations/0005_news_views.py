# Generated by Django 5.1 on 2024-08-16 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0004_alter_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
