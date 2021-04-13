# Generated by Django 3.1.7 on 2021-04-06 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0001_initial'),
        ('users', '0002_auto_20210406_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missionuser',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='missionusers', to='missions.mission'),
        ),
        migrations.AlterField(
            model_name='missionuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='missionusers', to=settings.AUTH_USER_MODEL),
        ),
    ]
