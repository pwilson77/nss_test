# Generated by Django 2.2.3 on 2019-07-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datamodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('age', models.IntegerField()),
                ('gender', models.TextField()),
                ('address', models.TextField()),
            ],
        ),
    ]
