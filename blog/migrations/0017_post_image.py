# Generated by Django 4.2.7 on 2024-02-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Image',
            field=models.ImageField(default='blog/NaNN.jpg', upload_to='blog/'),
        ),
    ]