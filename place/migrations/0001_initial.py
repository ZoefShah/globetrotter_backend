# Generated by Django 2.1 on 2018-08-30 10:57

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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentNext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='placeImage')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Views', models.IntegerField(default=0)),
                ('Likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.TextField()),
                ('Best_time_to_visit', models.CharField(max_length=255)),
                ('Dont_miss', models.TextField()),
                ('Things_to_avoid', models.TextField()),
                ('Means_of_transport', models.TextField()),
                ('Place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.Place')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='user_exp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.UserExperience'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_exp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.UserExperience'),
        ),
    ]
