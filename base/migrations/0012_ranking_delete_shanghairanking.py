# Generated by Django 4.2.1 on 2023-06-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_shanghairanking_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('year', models.CharField(max_length=200, null=True)),
                ('ranking', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ShanghaiRanking',
        ),
    ]