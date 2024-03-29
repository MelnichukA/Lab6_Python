# Generated by Django 2.2.7 on 2019-12-09 16:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('docxtopdf', '0005_auto_20191209_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='userName',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='pdfconverter',
            name='user',
            field=models.ForeignKey(null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, to='docxtopdf.UserInfo'),
            preserve_default=False,
        ),
    ]
