# Generated by Django 3.1.4 on 2020-12-19 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0006_auto_20201219_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('user_id', models.IntegerField(default='-1', primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
