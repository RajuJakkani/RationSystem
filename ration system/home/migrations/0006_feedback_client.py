# Generated by Django 4.2 on 2023-04-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_feedback_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='client',
            field=models.CharField(default=123, max_length=100),
        ),
    ]
