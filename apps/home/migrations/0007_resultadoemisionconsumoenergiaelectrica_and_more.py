# Generated by Django 4.2.1 on 2023-06-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_consumo_energia_electrica_alcance2_consumo_energia_electrica_kwh'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoEmisionConsumoEnergiaelectrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResultadoEmisionConsumoEnergiaelectrica', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Emisión por Consumo de energía eléctrica (KgCO2)',
                'verbose_name_plural': 'Emisiones por Consumo de energía eléctrica (KgCO2)',
            },
        ),
        migrations.CreateModel(
            name='ResultadoEmisionGasRefrigerante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResultadoEmisionGasRefrigerante', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Emisión de Gas Refrigerante (KgCO2)',
                'verbose_name_plural': 'Emisioes de Gases Refrigerantes (KgCO2)',
            },
        ),
    ]