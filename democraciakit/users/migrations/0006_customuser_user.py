# Generated by Django 5.1 on 2024-08-13 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
