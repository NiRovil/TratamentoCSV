# Generated by Django 4.0.3 on 2022-05-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelomovimento',
            name='data_e_hora_da_transacao',
            field=models.DateField(),
        ),
    ]
