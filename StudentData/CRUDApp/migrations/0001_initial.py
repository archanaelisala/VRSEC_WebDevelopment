# Generated by Django 3.1.4 on 2021-04-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studentdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=60)),
                ('Password', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=100)),
                ('Mobile', models.IntegerField(null=True)),
            ],
        ),
    ]
