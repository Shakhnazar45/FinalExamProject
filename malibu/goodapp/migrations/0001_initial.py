# Generated by Django 3.2.8 on 2021-11-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('url', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Surname', models.CharField(max_length=20)),
                ('PhoneNumber', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodcount', models.CharField(max_length=200)),
                ('all_price', models.PositiveIntegerField()),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodapp.market')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goodapp.user')),
            ],
        ),
    ]
