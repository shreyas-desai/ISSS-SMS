# Generated by Django 5.1.2 on 2024-12-02 20:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewPortal', '0012_contacts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='academic_dept',
        ),
        migrations.RemoveField(
            model_name='student',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='student',
            name='major',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_status',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_sub_type',
        ),
        migrations.RemoveField(
            model_name='student',
            name='profile_type',
        ),
        migrations.RemoveField(
            model_name='student',
            name='start_date',
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_type', models.CharField(max_length=10)),
                ('profile_sub_type', models.CharField(max_length=10)),
                ('profile_status', models.BooleanField()),
                ('profile_sub_status', models.CharField(max_length=10)),
                ('sponsorship', models.CharField(max_length=10)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('academic_dept', models.CharField(choices=[('sch', 'Scahefer'), ('bus', 'business')], max_length=10)),
                ('major', models.CharField(choices=[('CS', 'Computer Science'), ('MIS', 'Information Systems')], max_length=10)),
                ('student_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='renewPortal.student')),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_file', models.FileField(upload_to='documents/profiles/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='renewPortal.profiles')),
            ],
        ),
    ]
