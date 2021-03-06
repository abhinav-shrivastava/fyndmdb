# Generated by Django 2.0.5 on 2018-05-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('imdb_score', models.DecimalField(decimal_places=1, max_digits=4)),
                ('popularity', models.DecimalField(decimal_places=1, max_digits=4)),
                ('genre', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
