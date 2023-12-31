# Generated by Django 5.0 on 2023-12-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
                ('aadhar_card_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
