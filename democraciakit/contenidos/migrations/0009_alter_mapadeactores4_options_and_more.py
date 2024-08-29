# Generated by Django 5.1 on 2024-08-29 02:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenidos', '0008_alter_inclusivo2_cinco_alter_inclusivo2_cuatro_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mapadeactores4',
            options={'ordering': ['-fecha_mapadeactores2'], 'verbose_name': 'Etapa #4 - Mapa de actores', 'verbose_name_plural': 'Etapa #4 - Mapa de actores'},
        ),
        migrations.AlterField(
            model_name='mapadeactores4',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mapadeactores4_usuarios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Oportunidades4',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uno', models.TextField(blank=True, null=True)),
                ('dos', models.TextField(blank=True, null=True)),
                ('fecha_oportunidades4', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oportunidades4_usuarios', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Etapa #4 - Oportunidades',
                'verbose_name_plural': 'Etapa #4 - Oportunidades',
                'ordering': ['-fecha_oportunidades4'],
                'unique_together': {('usuario', 'fecha_oportunidades4')},
            },
        ),
    ]