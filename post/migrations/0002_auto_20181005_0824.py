# Generated by Django 2.1.2 on 2018-10-05 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
