# Generated by Django 4.0.1 on 2022-01-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('diary_cnt', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('content', models.CharField(max_length=500)),
                ('edit_date', models.DateTimeField()),
                ('write_date', models.DateTimeField()),
                ('diary_date', models.DateField()),
            ],
        ),
    ]