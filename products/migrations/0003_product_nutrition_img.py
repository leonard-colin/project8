# Generated by Django 3.1.6 on 2021-02-16 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210215_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutrition_img',
            field=models.URLField(blank=True),
        ),
    ]
