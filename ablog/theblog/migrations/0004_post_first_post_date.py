# Generated by Django 4.1.4 on 2023-01-07 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_post_post_date_alter_post_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='first_post_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
