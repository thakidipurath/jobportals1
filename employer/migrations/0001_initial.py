# Generated by Django 4.0.1 on 2022-03-15 13:57

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
            name='EmployerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('skill', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=150)),
                ('posted_date', models.DateField(auto_now_add=True, null=True)),
                ('last_date', models.DateField()),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employer.employerprofile')),
            ],
        ),
    ]
