# Generated by Django 3.2.15 on 2022-09-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demonstration', '0002_alter_resultadoshistorial_historial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='busqueda',
            field=models.CharField(default='', max_length=100),
        ),
    ]
