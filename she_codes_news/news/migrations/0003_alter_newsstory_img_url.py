# Generated by Django 4.0.1 on 2022-06-03 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsstory_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='img_url',
            field=models.URLField(),
        ),
    ]
