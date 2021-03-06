# Generated by Django 4.0 on 2022-01-25 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_assign_store_size'),
        ('cloud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileFolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_id', models.IntegerField(default=1)),
                ('folder_name', models.CharField(max_length=300)),
                ('share_id', models.IntegerField(default=0)),
                ('upper_folder_id', models.IntegerField()),
                ('level', models.IntegerField(default=0)),
                ('oner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oner_id', to='account.account')),
            ],
        ),
        migrations.AddField(
            model_name='storefile',
            name='folder_id',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='ShareStoreFile',
        ),
    ]
