# Generated by Django 5.1.3 on 2024-11-07 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='streaming',
            field=models.CharField(choices=[('AK', 'Amazon Kindle'), ('F', 'Fisico')], default='AB', max_length=2),
        ),
    ]
