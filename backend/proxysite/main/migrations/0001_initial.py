# Generated by Django 3.1.6 on 2021-02-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('proxyType', models.CharField(choices=[(0, 'HTTP'), (1, 'HTTPS'), (2, 'SOCKS5'), (3, 'SOCKS4')], max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('ping_to_google', models.IntegerField()),
                ('ping_to_yandex', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UpdateTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('checked_proxy', models.IntegerField()),
                ('good_proxy', models.IntegerField()),
            ],
        ),
    ]
