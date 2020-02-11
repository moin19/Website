# Generated by Django 3.0.2 on 2020-01-23 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaCode', models.CharField(max_length=200)),
                ('contry', models.TextField()),
                ('reporter_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Reporter')),
            ],
        ),
    ]
