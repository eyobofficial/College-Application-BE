# Generated by Django 2.2 on 2019-04-12 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('short_name', models.CharField(max_length=30, unique=True)),
                ('summary', models.TextField(blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.CharField(max_length=60)),
                ('link', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('degree_type', models.CharField(choices=[('BD', 'Bachelor'), ('MD', 'Masters'), ('PD', 'Ph.D')], max_length=2)),
                ('summary', models.TextField(blank=True)),
                ('program_start_date', models.DateField(blank=True, null=True)),
                ('application_start_date', models.DateField()),
                ('application_end_date', models.DateField()),
                ('link', models.URLField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='programs', to='programs.College')),
            ],
            options={
                'ordering': ('title',),
                'default_related_name': 'programs',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('is_optional', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='programs.Program')),
            ],
            options={
                'default_related_name': 'requirements',
                'order_with_respect_to': 'program',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('IP', 'In Progress'), ('SU', 'Submitted'), ('AC', 'Accepted'), ('RE', 'Rejected')], default='IP', max_length=2)),
                ('remark', models.TextField(blank=True)),
                ('link', models.URLField(blank=True, max_length=255)),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('completed_requirements', models.ManyToManyField(related_name='applications', to='programs.Requirement')),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='programs.Program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-started_at',),
                'default_related_name': 'applications',
            },
        ),
    ]