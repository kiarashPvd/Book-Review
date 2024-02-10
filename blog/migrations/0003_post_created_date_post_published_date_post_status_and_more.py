# Generated by Django 4.2.7 on 2024-02-10 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_counted_veiws'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='counted_veiws',
            field=models.IntegerField(),
        ),
    ]
