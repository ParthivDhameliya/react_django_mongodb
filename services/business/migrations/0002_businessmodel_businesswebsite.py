# Generated by Django 4.1.4 on 2022-12-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessmodel',
            name='businessWebsite',
            field=models.URLField(default=''),
        ),
    ]
