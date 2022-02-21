# Generated by Django 4.0 on 2022-02-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0003_remove_filefolder_share_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharefolder',
            name='share_folder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share_folder_id', to='cloud.filefolder'),
        ),
        migrations.AlterField(
            model_name='storefile',
            name='belong_folder_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belong_folder_id', to='cloud.filefolder'),
        ),
    ]
