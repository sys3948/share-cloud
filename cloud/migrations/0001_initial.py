# Generated by Django 4.0 on 2022-01-05 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.FileField(upload_to='')),
                ('file_name', models.CharField(max_length=300)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='ShareStoreFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shareuser', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='share_account', to='account.account')),
                ('storefile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storefile', to='cloud.storefile')),
            ],
        ),
    ]
