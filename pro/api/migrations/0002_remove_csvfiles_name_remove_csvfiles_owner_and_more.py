# Generated by Django 4.1.5 on 2023-01-19 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csvfiles',
            name='name',
        ),
        migrations.RemoveField(
            model_name='csvfiles',
            name='owner',
        ),
        migrations.AddField(
            model_name='csvfiles',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]