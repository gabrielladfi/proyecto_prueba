# Generated by Django 4.2.1 on 2024-12-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_customuser_id_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id_perfil',
            field=models.CharField(default='d11ba0c70b044634a03d854e7b3fb941', editable=False, max_length=32),
        ),
    ]
