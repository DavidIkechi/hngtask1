# Generated by Django 4.1.2 on 2022-10-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HNGUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slackUsername', models.CharField(max_length=100)),
                ('backend', models.BooleanField(default=False)),
                ('age', models.IntegerField(default=0)),
                ('bio', models.CharField(max_length=1000)),
            ],
        ),
    ]