# Generated by Django 5.0.2 on 2024-03-01 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
                ('disk_total', models.BigIntegerField()),
                ('disk_used', models.BigIntegerField()),
                ('disk_free', models.BigIntegerField()),
                ('main_process_id', models.IntegerField()),
                ('memory_ram', models.IntegerField()),
                ('ip_address', models.GenericIPAddressField()),
                ('last_update', models.DateTimeField()),
            ],
        ),
    ]
