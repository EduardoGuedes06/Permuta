# Generated by Django 3.2.7 on 2022-07-01 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_auto_20220627_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permuta',
            name='Motivo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='permuta',
            name='NomePacOf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastros.vagaof'),
        ),
    ]
