# Generated by Django 4.2.3 on 2023-10-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('designation', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=200)),
                ('contact', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('type', models.CharField(max_length=33)),
                ('illiness', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=300)),
                ('contact', models.BigIntegerField()),
            ],
        ),
    ]