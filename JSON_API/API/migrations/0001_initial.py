# Generated by Django 3.2.6 on 2021-08-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cldr',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='volume')),
            ],
            options={
                'db_table': 'cldr',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Docu',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='volume')),
            ],
            options={
                'db_table': 'docu',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pd',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'pd',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pins',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='volume')),
            ],
            options={
                'db_table': 'pins',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pvl',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(primary_key=True, serialize=False, verbose_name='volume')),
            ],
            options={
                'db_table': 'pvl',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(primary_key=True, serialize=False, verbose_name='volume')),
            ],
            options={
                'db_table': 'run',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zm',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='volume')),
            ],
            options={
                'db_table': 'zm',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Zuo',
            fields=[
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('adj_close', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'zuo',
                'managed': True,
            },
        ),
    ]