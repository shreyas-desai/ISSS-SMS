# Generated by Django 5.1.2 on 2024-11-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewPortal', '0004_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='portal_access',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='sso',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='stage_status',
            field=models.CharField(choices=[('check-in', 'Check In'), ('continuing', 'Continuing'), ('pre-arrival', 'Pre Arrival'), ('post-grad', 'Postcompletion Graduated')], default='Continuing', max_length=30),
            preserve_default=False,
        ),
    ]
