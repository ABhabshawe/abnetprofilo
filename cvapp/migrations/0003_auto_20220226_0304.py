# Generated by Django 3.2.4 on 2022-02-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_feedbackform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(),
        ),
    ]
