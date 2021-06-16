# Generated by Django 3.2.3 on 2021-06-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=256)),
                ('desc', models.TextField(max_length=512)),
                ('isDone', models.BooleanField(verbose_name=False)),
                ('timeStamp', models.DateTimeField()),
            ],
        ),
    ]