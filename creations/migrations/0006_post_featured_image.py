# Generated by Django 2.2.7 on 2020-01-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0005_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='', upload_to='blogImages'),
        ),
    ]