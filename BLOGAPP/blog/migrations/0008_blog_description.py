# Generated by Django 4.0.6 on 2022-07-29 12:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(default=2),
            preserve_default=False,
        ),
    ]