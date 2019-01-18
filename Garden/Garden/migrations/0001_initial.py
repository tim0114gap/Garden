# Generated by Django 2.1.4 on 2019-01-18 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20, null=True)),
                ('text', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='UserLists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=20)),
            ],
        ),
    ]
