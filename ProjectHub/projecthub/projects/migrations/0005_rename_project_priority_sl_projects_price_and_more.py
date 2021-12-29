# Generated by Django 4.0 on 2021-12-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20211130_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_priority_sl',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='demo_link',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='source_link',
        ),
        migrations.AddField(
            model_name='projects',
            name='location',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='owner_name',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]