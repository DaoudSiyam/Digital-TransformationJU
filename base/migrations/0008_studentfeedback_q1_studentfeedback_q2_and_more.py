# Generated by Django 4.2.1 on 2023-06-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_qsranking_ranking_qsranking_subject_qsranking_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentfeedback',
            name='q1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentfeedback',
            name='q2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentfeedback',
            name='q3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentfeedback',
            name='q4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentfeedback',
            name='q5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studentfeedback',
            name='q6',
            field=models.IntegerField(default=0),
        ),
    ]
