# Generated by Django 4.1.7 on 2024-01-14 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_information_added_alter_information_impact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='added',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='country',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='end_year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='impact',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='insight',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='intensity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='likelihood',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='pestle',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='published',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='region',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='relevance',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='sector',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='source',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='start_year',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='topic',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='information',
            name='url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
