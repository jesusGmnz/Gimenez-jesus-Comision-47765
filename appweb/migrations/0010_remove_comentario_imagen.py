# Generated by Django 4.2.5 on 2023-10-27 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0009_alter_comentario_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='imagen',
        ),
    ]