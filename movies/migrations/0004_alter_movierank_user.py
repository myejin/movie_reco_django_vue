# Generated by Django 3.2.9 on 2021-11-19 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_genre_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierank',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranks', to=settings.AUTH_USER_MODEL),
        ),
    ]
