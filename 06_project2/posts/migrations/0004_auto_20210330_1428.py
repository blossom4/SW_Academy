# Generated by Django 3.1.7 on 2021-03-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210330_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster_path',
            field=models.CharField(default='https://data.ac-illust.com/data/thumbnails/2a/2a2127b1c718e4c2c056eddf3b505dc0_t.jpeg', max_length=300),
        ),
    ]
