# Generated by Django 5.0.6 on 2024-06-20 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='Categorys',
        ),
    ]
