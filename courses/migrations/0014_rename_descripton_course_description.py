# Generated by Django 4.0.5 on 2022-06-30 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_homework_pub_date_alter_homework_return_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='descripton',
            new_name='description',
        ),
    ]