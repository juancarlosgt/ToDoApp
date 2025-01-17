# Generated by Django 5.0.3 on 2024-05-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_task_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("low", "Low"), ("medium", "Medium"), ("high", "High")],
                default="low",
                max_length=10,
            ),
        ),
    ]
