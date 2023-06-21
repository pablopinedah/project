# Generated by Django 4.2.1 on 2023-06-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alcance1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refrigerante', models.CharField(max_length=20)),
                ('cantidad_refrigerante_kg', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Alcance2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumo_energia_electrica_kwh', models.FloatField()),
                ('mes', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=20)),
                ('pais', models.CharField(default='', max_length=20)),
                ('numero_empleados', models.IntegerField(blank=True, default=1, null=True)),
                ('año_datos', models.IntegerField(blank=True, default=2020, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Factor_emision_consumo_energiaelectrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PAIS', models.CharField(default='', max_length=20)),
                ('AÑO_FACTOR_EMISION', models.IntegerField(blank=True, default=2020, null=True)),
                ('FACTOR_EMISION_ELECTRICIDAD', models.FloatField()),
            ],
            options={
                'verbose_name': 'Factor de emisión por consumo de energía (kg CO2e/kWh)',
                'verbose_name_plural': 'Factores de emisión por consumo de energía (kg CO2e/kWh)',
                'ordering': ['AÑO_FACTOR_EMISION'],
            },
        ),
        migrations.CreateModel(
            name='Factor_emision_gas_refrigerante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIPO_REFRIGERANTE', models.CharField(max_length=20)),
                ('GWP', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tipo de Refrigerante (AR5)',
                'verbose_name_plural': 'Tipos de Refrigerantes (AR5)',
            },
        ),
        migrations.CreateModel(
            name='ResultadoEmisionConsumoEnergiaelectrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
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
                ('valor', models.FloatField()),
            ],
            options={
                'verbose_name': 'Emisión de Gas Refrigerante (KgCO2)',
                'verbose_name_plural': 'Emisioes de Gases Refrigerantes (KgCO2)',
            },
        ),
    ]
