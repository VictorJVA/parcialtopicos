# Generated by Django 4.2.4 on 2024-09-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('price', models.FloatField()),
            ],
        ),
    ]
