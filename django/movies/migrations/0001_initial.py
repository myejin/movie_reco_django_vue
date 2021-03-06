# Generated by Django 3.2.9 on 2021-11-18 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('profile_path', models.TextField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('overview', models.TextField(default=False)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('poster_path', models.TextField(default=False)),
                ('director', models.CharField(default=False, max_length=50)),
                ('rate_user_count', models.IntegerField()),
                ('total_rank', models.IntegerField()),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.Actor')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='MovieRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(choices=[(1, '1'), (2, '3'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='rate_users',
            field=models.ManyToManyField(related_name='rate_movies', through='movies.MovieRank', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='wish_users',
            field=models.ManyToManyField(related_name='wish_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
