# Generated by Django 3.1.2 on 2020-11-03 19:41

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_autor_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=ckeditor.fields.RichTextField(verbose_name='Descripcion'),
        ),
    ]
