# Generated by Django 3.0.4 on 2020-03-21 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0004_auto_20200321_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='is_complex',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
