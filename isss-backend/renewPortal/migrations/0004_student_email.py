# Generated by Django 5.1.2 on 2024-11-08 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewPortal', '0003_student_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='abc.xyz@.com', max_length=254),
            preserve_default=False,
        ),
    ]
