# Generated by Django 4.2.7 on 2024-03-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.DateField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
