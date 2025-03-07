# Generated by Django 5.1.6 on 2025-02-09 17:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date_time', models.DateTimeField(auto_now_add=True)),
                ('model_no', models.CharField(max_length=50)),
                ('qty', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('dispatch_id', models.AutoField(primary_key=True, serialize=False)),
                ('dispatch_person', models.CharField(max_length=100)),
                ('dispatch_date_time', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='Received',
            fields=[
                ('received_id', models.AutoField(primary_key=True, serialize=False)),
                ('received_person', models.CharField(max_length=100)),
                ('received_date_time', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
