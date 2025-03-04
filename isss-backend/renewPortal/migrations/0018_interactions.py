# Generated by Django 5.1.2 on 2024-12-10 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewPortal', '0017_custom_studentdocuments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_type', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('advisor', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=200)),
                ('student_interactions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='renewPortal.student')),
            ],
        ),
    ]
