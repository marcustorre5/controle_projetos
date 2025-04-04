# Generated by Django 5.1.7 on 2025-03-29 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0003_projeto_descricao_alter_projeto_data_fim_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='cliente',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='status',
            field=models.CharField(choices=[('em_andamento', 'Em Andamento'), ('finalizado', 'Finalizado'), ('revisao', 'Revisão')], default='em_andamento', max_length=50),
        ),
    ]
