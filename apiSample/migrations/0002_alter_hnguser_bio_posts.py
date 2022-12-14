# Generated by Django 4.1.2 on 2022-10-29 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiSample', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hnguser',
            name='bio',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiSample.hnguser')),
            ],
        ),
    ]
