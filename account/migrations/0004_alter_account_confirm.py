# Generated by Django 4.0 on 2022-01-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='confirm',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
