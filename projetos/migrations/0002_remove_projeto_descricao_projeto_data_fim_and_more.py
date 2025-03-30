# projetos/migrations/0002_auto_20250329_1234.py
from django.db import migrations, models
import django.db.models.deletion

def set_default_data_fim(apps, schema_editor):
    Projeto = apps.get_model('projetos', 'Projeto')
    Projeto.objects.filter(data_fim__isnull=True).update(data_fim='2025-01-01')

class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='data_fim',
            field=models.DateField(null=False),
        ),
        migrations.RunPython(set_default_data_fim),
    ]
