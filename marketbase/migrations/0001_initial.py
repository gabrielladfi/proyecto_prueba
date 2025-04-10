# Generated by Django 4.2.1 on 2025-04-04 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CampaignMain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('call_action01', models.CharField(max_length=300)),
                ('call_action02', models.CharField(max_length=300)),
                ('call_action03', models.CharField(max_length=300)),
                ('about_us', models.CharField(max_length=500)),
                ('beneficios_clave', models.CharField(max_length=500)),
                ('testimonials', models.CharField(max_length=500)),
                ('faqs', models.CharField(max_length=500)),
                ('wireframe_type', models.CharField(max_length=200)),
                ('campaign', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='landing', to='marketbase.campaignmain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('problem', models.CharField(max_length=400)),
                ('target_age', models.CharField(max_length=3)),
                ('target_location', models.CharField(max_length=150)),
                ('target_interest', models.CharField(max_length=250)),
                ('differential_factor', models.CharField(max_length=250)),
                ('communication_type', models.CharField(max_length=15)),
                ('call_actions', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_base', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
