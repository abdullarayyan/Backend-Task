# Generated by Django 3.1.4 on 2020-12-19 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0004_auto_20201219_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofiledb',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', user_profile.models.EnumField(choices=[('m', 'Male'), ('f', 'Female')])),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.IntegerField(default='-1', primary_key=True, serialize=False)),
                ('maital_status', models.IntegerField(choices=[('s', 'Single'), ('m', 'Married'), ('D', 'Divorced')])),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile_User',
        ),
    ]
