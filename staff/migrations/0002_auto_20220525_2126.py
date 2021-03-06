# Generated by Django 3.2.12 on 2022-05-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='priority',
            field=models.IntegerField(default=1000, verbose_name='приоритет'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='posttype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
    ]
