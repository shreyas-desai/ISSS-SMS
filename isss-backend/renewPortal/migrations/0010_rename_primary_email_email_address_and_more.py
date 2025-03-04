# Generated by Django 5.1.2 on 2024-11-26 19:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewPortal', '0009_rename_student_address_student_address_dependents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='primary',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='secondary',
            new_name='email_type',
        ),
        migrations.RemoveField(
            model_name='email',
            name='student',
        ),
        migrations.AddField(
            model_name='email',
            name='student_emails',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='renewPortal.student'),
            preserve_default=False,
        ),
    ]
