# Generated by Django 5.1.5 on 2025-02-03 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='createdBy',
            field=models.CharField(default=models.CharField(max_length=255, unique=True), max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='createdOn',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='modifiedBy',
            field=models.CharField(default='yet to be modified', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='modifiedOn',
            field=models.DateTimeField(null=True),
        ),
    ]
