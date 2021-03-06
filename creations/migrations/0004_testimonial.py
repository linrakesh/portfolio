# Generated by Django 2.2.7 on 2020-01-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creations', '0003_option_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='testimonial')),
            ],
        ),
    ]
