# Generated by Django 3.2.7 on 2022-07-04 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_vagaofertada_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permuta',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='vagaofertada',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='permuta',
            name='data_inclusao',
        ),
        migrations.RemoveField(
            model_name='vagaofertada',
            name='data_inclusao',
        ),
        migrations.AlterField(
            model_name='permuta',
            name='data_vagaOfertada',
            field=models.DateTimeField(verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='permuta',
            name='nomePacienteAgendado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nomePacienteAgendado', to='cadastros.paciente', verbose_name='Paciente Para Agendar'),
        ),
        migrations.AlterField(
            model_name='permuta',
            name='nomePacienteOfertado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='nomePacienteOfertado', to='cadastros.paciente'),
        ),
        migrations.AlterField(
            model_name='permuta',
            name='procedimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.procedimento', verbose_name='Procedimento'),
        ),
        migrations.AlterField(
            model_name='permuta',
            name='unidadeExecutante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.unidadeexecutante', verbose_name='Unidade Executante'),
        ),
        migrations.AlterField(
            model_name='vagaofertada',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.paciente', verbose_name='Nome do Paciente'),
        ),
        migrations.AlterField(
            model_name='vagaofertada',
            name='procedimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.procedimento', verbose_name='Procedimento'),
        ),
        migrations.AlterField(
            model_name='vagaofertada',
            name='unidadeExecutante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.unidadeexecutante', verbose_name='Unidade Executante'),
        ),
    ]
