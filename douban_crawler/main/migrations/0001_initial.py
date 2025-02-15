# Generated by Django 5.1.6 on 2025-02-08 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('detail_url', models.CharField(max_length=2000)),
                ('img_url', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=200)),
                ('name_foreign', models.CharField(max_length=200)),
                ('grade', models.FloatField(default=0.0)),
                ('num_evaluate', models.BigIntegerField(default=0)),
                ('sketch', models.CharField(max_length=2000)),
                ('other_info', models.CharField(max_length=2000)),
            ],
        ),
    ]
