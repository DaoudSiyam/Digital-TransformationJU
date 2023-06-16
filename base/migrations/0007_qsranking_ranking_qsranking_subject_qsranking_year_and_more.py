# Generated by Django 4.2.1 on 2023-06-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_shanghairanking_ranking_shanghairanking_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='qsranking',
            name='ranking',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qsranking',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='qsranking',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='theranking',
            name='ranking',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='theranking',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='theranking',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='webometricsranking',
            name='ranking',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='webometricsranking',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='webometricsranking',
            name='year',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='workerfeedback',
            name='q1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workerfeedback',
            name='q2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workerfeedback',
            name='q3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workerfeedback',
            name='q4',
            field=models.IntegerField(default=0),
        ),
    ]