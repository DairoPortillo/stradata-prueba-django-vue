# Generated by Django 3.2.15 on 2022-09-19 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demonstration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultadoshistorial',
            name='historial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='resultados_historial', to='demonstration.historial'),
        ),
    ]
