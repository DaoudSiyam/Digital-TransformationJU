# Generated by Django 4.2.1 on 2023-06-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_feedback_q12'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='full_name',
        ),
    ]