# Generated by Django 4.2.1 on 2025-03-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CanvasModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('value_proposition', models.TextField(blank=True, null=True)),
                ('customer_segments', models.TextField(blank=True, null=True)),
                ('channels', models.TextField(blank=True, null=True)),
                ('customer_relationships', models.TextField(blank=True, null=True)),
                ('revenue_streams', models.TextField(blank=True, null=True)),
                ('key_resources', models.TextField(blank=True, null=True)),
                ('key_activities', models.TextField(blank=True, null=True)),
                ('key_partners', models.TextField(blank=True, null=True)),
                ('cost_structure', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
