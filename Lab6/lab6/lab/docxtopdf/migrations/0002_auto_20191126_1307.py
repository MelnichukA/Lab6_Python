# Generated by Django 2.2.7 on 2019-11-26 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docxtopdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfconverter',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
