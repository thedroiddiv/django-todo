# Generated by Django 3.2.4 on 2021-06-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_auto_20210616_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]