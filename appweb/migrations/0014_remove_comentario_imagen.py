# Generated by Django 4.2.5 on 2023-10-29 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0013_alter_comentario_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='imagen',
        ),
    ]