# Generated by Django 4.0.6 on 2022-08-24 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.AutoField(primary_key=True, serialize=False)),
                ('name_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id_position', models.AutoField(primary_key=True, serialize=False)),
                ('name_position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.AutoField(primary_key=True, serialize=False)),
                ('name_dish', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.category')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id_employee', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('second_name', models.CharField(max_length=45)),
                ('first_lastname', models.CharField(max_length=45)),
                ('second_lastname', models.CharField(max_length=45)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.category')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.position')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.user')),
            ],
        ),
    ]