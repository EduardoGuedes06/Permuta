# Generated by Django 3.2.7 on 2022-07-12 23:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0016_remove_unidadesolicitante_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserUnidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidadeSolicitante', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cadastros.unidadesolicitante', verbose_name='Unidade')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
