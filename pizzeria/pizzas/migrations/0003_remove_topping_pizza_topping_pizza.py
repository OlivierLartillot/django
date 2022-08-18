# Generated by Django 4.1 on 2022-08-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_topping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='pizza',
        ),
        migrations.AddField(
            model_name='topping',
            name='pizza',
            field=models.ManyToManyField(to='pizzas.pizza'),
        ),
    ]