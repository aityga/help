# Generated by Django 3.2.8 on 2021-11-10 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laptop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='battery',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='brand',
            field=models.CharField(blank=True, choices=[(1, 'apple'), (2, 'asus'), (3, 'dell'), (4, 'acer'), (5, 'lenovo')], max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='color',
            field=models.CharField(blank=True, choices=[(1, 'grey'), (2, 'silver'), (3, 'black'), (4, 'red'), (5, 'blue')], max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='cpu',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='display',
            field=models.CharField(blank=True, choices=[(1, '4096 x 2160'), (2, '2048 x 1080'), (3, '1920 x 1080'), (4, '1024 x 768')], max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='memory',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='prod',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='ram',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='vin',
            field=models.IntegerField(blank=True),
        ),
    ]
