# Generated by Django 4.2.7 on 2024-02-03 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpage',
            name='status',
            field=models.CharField(choices=[('OFF', 'Offline'), ('ON', 'Online')], default='OFF', max_length=3),
        ),
        migrations.AddField(
            model_name='userpage',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
