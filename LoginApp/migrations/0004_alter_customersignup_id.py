# Generated by Django 4.2.2 on 2023-10-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginApp', '0003_rename_user_customersignup_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersignup',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]