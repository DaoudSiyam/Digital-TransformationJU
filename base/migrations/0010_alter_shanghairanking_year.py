# Generated by Django 4.2.1 on 2023-06-16 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shanghairanking',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]