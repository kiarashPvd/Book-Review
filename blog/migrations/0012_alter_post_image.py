# Generated by Django 4.2.7 on 2024-02-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/NaN.jpg', upload_to='blog/'),
        ),
    ]