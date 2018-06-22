# Generated by Django 2.1a1 on 2018-06-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('open1', models.FloatField()),
                ('close', models.FloatField()),
                ('Volume', models.IntegerField()),
            ],
        ),
    ]
