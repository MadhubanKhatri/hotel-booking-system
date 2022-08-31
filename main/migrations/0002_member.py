# Generated by Django 3.0.11 on 2022-08-26 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact_number', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('ac_opt', models.CharField(max_length=50)),
                ('bad_opt', models.CharField(max_length=50)),
                ('room_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Room')),
            ],
        ),
    ]