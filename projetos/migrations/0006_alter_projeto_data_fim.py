# Generated by Django 5.1.7 on 2025-03-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0005_remove_projeto_cliente_remove_projeto_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='data_fim',
            field=models.DateField(),
        ),
    ]
