# Generated by Django 4.1.8 on 2023-05-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_contact_us'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idx', models.IntegerField()),
                ('task', models.CharField(max_length=100)),
            ],
        ),
    ]
