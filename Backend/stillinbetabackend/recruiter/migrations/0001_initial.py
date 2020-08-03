# Generated by Django 3.0.8 on 2020-08-02 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recruiter.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtractJD',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('jd', models.FileField(upload_to=recruiter.models.recruiter_jd_extract)),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('address_line1', models.CharField(max_length=40)),
                ('address_line2', models.CharField(blank=True, max_length=40)),
                ('mobile_number', models.CharField(max_length=12)),
                ('display_name', models.CharField(max_length=255)),
                ('pan_number', models.CharField(max_length=20)),
                ('website', models.URLField(blank=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=recruiter.models.recruiter_logo)),
                ('bio', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobCreation',
            fields=[
                ('jobid', models.BigAutoField(primary_key=True, serialize=False)),
                ('skills', models.CharField(max_length=255)),
                ('email_id', models.EmailField(max_length=255)),
                ('job_title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
                ('total_vacancy', models.PositiveIntegerField()),
                ('salary', models.CharField(max_length=255)),
                ('jd', models.FileField(upload_to=recruiter.models.recruiter_jd)),
                ('summary', models.TextField(blank=True)),
                ('tags', models.TextField(blank=True)),
                ('activate', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('job_type', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.Recruiter')),
            ],
        ),
    ]