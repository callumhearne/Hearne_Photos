# Generated by Django 3.2 on 2021-04-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_alter_photo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]
