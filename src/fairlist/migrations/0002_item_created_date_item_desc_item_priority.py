# Generated by Django 4.2.3 on 2023-07-21 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fairlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='priority',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]