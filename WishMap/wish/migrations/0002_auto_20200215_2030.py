# Generated by Django 3.0.3 on 2020-02-15 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wish',
            name='visibility',
            field=models.IntegerField(choices=[(1, 'Me'), (2, 'Friends'), (3, 'All')], default=1),
            preserve_default=False,
        ),
    ]
