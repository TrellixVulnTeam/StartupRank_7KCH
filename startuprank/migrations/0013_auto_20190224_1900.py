# Generated by Django 2.1.7 on 2019-02-24 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('startuprank', '0012_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='startup',
        ),
        migrations.DeleteModel(
            name='Votes',
        ),
    ]
