# Generated by Django 4.2.5 on 2023-10-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0011_alter_comentario_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='imagen',
            field=models.ImageField(null=True, upload_to='jabon'),
        ),
    ]
