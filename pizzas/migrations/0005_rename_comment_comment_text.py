# Generated by Django 3.2.10 on 2021-12-09 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='text',
        ),
    ]
