# Generated by Django 4.0 on 2022-03-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0009_remove_filefolder_share_able_filefolder_folder_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filefolder',
            name='folder_path',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='sharefolder',
            name='gropunum',
            field=models.IntegerField(),
        ),
    ]
