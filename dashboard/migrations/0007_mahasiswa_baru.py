# Generated by Django 5.1.4 on 2025-01-12 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_delete_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='mahasiswa_baru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=10)),
                ('nama', models.CharField(max_length=50)),
                ('prodi', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=4)),
                ('rencana_studi', models.BooleanField(default=False)),
            ],
        ),
    ]
