# Generated by Django 3.1.6 on 2021-03-10 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20210219_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='responsibilities',
        ),
        migrations.AddField(
            model_name='team',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='slack',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='about',
            field=models.TextField(default=''),
        ),
    ]
