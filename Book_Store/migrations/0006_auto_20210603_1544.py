# Generated by Django 2.2.3 on 2021-06-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Store', '0005_storebook_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='storebook',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='storebook',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]