# Generated by Django 4.2.1 on 2024-12-02 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_customuser_id_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id_perfil',
            field=models.CharField(default='114fed46f35e40f9b8df9828e234d896', editable=False, max_length=32),
        ),
    ]
