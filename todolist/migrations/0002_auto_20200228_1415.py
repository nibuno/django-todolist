# Generated by Django 2.2.10 on 2020-02-28 05:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2020, 2, 28, 5, 14, 51, 189681, tzinfo=utc), verbose_name='作成日'),
        ),
    ]
