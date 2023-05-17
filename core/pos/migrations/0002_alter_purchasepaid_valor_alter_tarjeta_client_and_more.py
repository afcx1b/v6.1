# Generated by Django 4.0.2 on 2023-04-26 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasepaid',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.client', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='cod_seguridad',
            field=models.CharField(max_length=4, verbose_name='Código de Seguridad'),
        ),
    ]