# Generated by Django 4.0.5 on 2022-07-02 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=100)),
                ('ingrendientes', models.TextField()),
                ('valor', models.FloatField()),
                ('imagem', models.ImageField(upload_to='')),
                ('categoria', models.CharField(max_length=100)),
                ('data_produto', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
