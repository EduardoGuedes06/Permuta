# Generated by Django 3.2.7 on 2022-07-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0010_auto_20220707_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vagaofertada',
            name='tipo',
            field=models.CharField(blank=True, choices=[('EXAME', 'EXAME'), ('CONSULTA', 'CONSULTA')], max_length=10, verbose_name='Tipo'),
        ),
    ]