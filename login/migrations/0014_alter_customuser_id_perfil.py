# Generated by Django 4.2.1 on 2025-03-31 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_alter_customuser_id_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id_perfil',
            field=models.CharField(default='ef415384527c429487eb98e3e7d77e1e', editable=False, max_length=32),
        ),
    ]
