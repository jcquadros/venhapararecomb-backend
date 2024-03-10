# Generated by Django 5.0.3 on 2024-03-10 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0004_remove_cliente_nota_fiscal_notafiscal_clientes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('cep', models.CharField(max_length=8)),
                ('pais', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='endereco',
            field=models.ForeignKey(default=-1991, on_delete=django.db.models.deletion.CASCADE, to='notafiscal.endereco'),
            preserve_default=False,
        ),
    ]
