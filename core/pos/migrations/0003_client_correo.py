# Generated by Django 4.0.2 on 2023-07-04 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0002_alter_purchasepaid_valor_alter_tarjeta_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='correo',
            field=models.CharField(default=1, max_length=150, unique=True, verbose_name='Correo electrónico'),
            preserve_default=False,
        ),
    ]