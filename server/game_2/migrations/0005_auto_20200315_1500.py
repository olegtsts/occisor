# Generated by Django 3.0.4 on 2020-03-15 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game_2', '0004_auto_20200315_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='creator',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='room_creator', to=settings.AUTH_USER_MODEL, verbose_name='room_creator'),
        ),
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.CharField(default='0', max_length=100),
        ),
    ]
