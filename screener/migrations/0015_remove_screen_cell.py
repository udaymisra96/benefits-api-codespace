# Generated by Django 4.0.5 on 2022-08-10 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screener', '0014_screen_cell_screen_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screen',
            name='cell',
        ),
    ]