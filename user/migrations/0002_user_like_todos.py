# Generated by Django 4.2.4 on 2023-09-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_comment'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_todos',
            field=models.ManyToManyField(related_name='like_users', to='todo.todo'),
        ),
    ]