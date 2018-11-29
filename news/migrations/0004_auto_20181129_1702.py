# Generated by Django 2.0.6 on 2018-11-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data created'),
        ),
        migrations.AddField(
            model_name='comments',
            name='moderration',
            field=models.BooleanField(default=False),
        ),
    ]
