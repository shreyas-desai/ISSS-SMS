# Generated by Django 5.1.2 on 2024-11-05 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renewPortal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='cwid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
