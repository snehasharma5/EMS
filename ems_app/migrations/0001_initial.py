# Generated by Django 4.2.6 on 2023-10-10 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_manager', models.BooleanField(default=False)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems_app.department')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems_app.employee')),
            ],
        ),
    ]
