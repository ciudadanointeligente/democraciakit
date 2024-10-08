# Generated by Django 5.1 on 2024-08-26 01:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0004_alter_definicion3_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Causas2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uno', models.TextField(blank=True, null=True)),
                ('dos', models.TextField(blank=True, null=True)),
                ('tres', models.TextField(blank=True, null=True)),
                ('cuatro', models.TextField(blank=True, null=True)),
                ('cinco', models.TextField(blank=True, null=True)),
                ('fecha_causas2', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='causas2_usuarios', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'fecha_causas2')},
            },
        ),
    ]
