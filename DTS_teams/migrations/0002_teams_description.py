# Generated by Django 2.0.5 on 2018-05-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DTS_teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='description',
            field=models.TextField(default='descriprion'),
            preserve_default=False,
        ),
    ]
