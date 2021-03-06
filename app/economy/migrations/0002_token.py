# Generated by Django 2.0.6 on 2018-07-02 19:30

from django.db import migrations, models
import economy.models


class Migration(migrations.Migration):

    dependencies = [
        ('economy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('address', models.CharField(db_index=True, max_length=255)),
                ('symbol', models.CharField(db_index=True, max_length=10)),
                ('network', models.CharField(db_index=True, max_length=25)),
                ('decimals', models.IntegerField(default=18)),
                ('priority', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
