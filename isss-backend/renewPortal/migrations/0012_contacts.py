# Generated by Django 5.1.2 on 2024-12-02 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewPortal', '0011_alter_email_email_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('P', 'Personal'), ('W', 'Work'), ('H', 'Home')], max_length=10)),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=20)),
                ('student_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='renewPortal.student')),
            ],
        ),
    ]
