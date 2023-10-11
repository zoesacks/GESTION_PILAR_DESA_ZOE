# Generated by Django 4.2.5 on 2023-09-16 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='solped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CODIGO', models.CharField(max_length=50)),
                ('DETALLE', models.TextField(blank=True, null=True)),
                ('NUMERO', models.CharField(max_length=50)),
                ('FECHA', models.DateField(blank=True, null=True)),
                ('TOTAL', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('NRO', models.CharField(blank=True, max_length=255, null=True)),
                ('SECRETARIA', models.CharField(blank=True, max_length=255, null=True)),
                ('SECRETARIA_NOMBRE', models.CharField(blank=True, max_length=255, null=True)),
                ('FONDO', models.CharField(blank=True, max_length=255, null=True)),
                ('CATEGORIA', models.CharField(blank=True, max_length=255, null=True)),
                ('FUENTE_FINANCIAMIENTO', models.CharField(blank=True, max_length=255, null=True)),
                ('COMENTARIOS', models.CharField(blank=True, max_length=50, null=True)),
                ('AUTORIZADO_POR', models.CharField(blank=True, max_length=255, null=True)),
                ('FECHA_AUTORIZADO', models.DateTimeField(blank=True, null=True)),
                ('ESTADO', models.BooleanField(default=0)),
                ('OBSERVADA', models.BooleanField(default=0)),
            ],
            options={
                'verbose_name': 'Solicitud de pedido',
                'verbose_name_plural': 'Solicitudes de pedidos',
            },
        ),
        migrations.CreateModel(
            name='productoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articulo', models.CharField(blank=True, max_length=255, null=True)),
                ('cantidad', models.DecimalField(decimal_places=2, default=1, max_digits=20)),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('objeto', models.CharField(blank=True, max_length=255, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='solicitud.solped')),
            ],
            options={
                'verbose_name': 'Articulos',
                'verbose_name_plural': 'Articulos incluidos en la solicitud',
            },
        ),
    ]
