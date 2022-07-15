# Generated by Django 3.2.7 on 2022-07-05 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_auto_20220704_1334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vagaofertada',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Vagas Ofertadas'},
        ),
        migrations.AddField(
            model_name='vagaofertada',
            name='unidadeSolicitante',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='cadastros.unidadesolicitante'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vagaofertada',
            name='status',
            field=models.BooleanField(blank=True, default=False, editable=False, null=True),
        ),
    ]
