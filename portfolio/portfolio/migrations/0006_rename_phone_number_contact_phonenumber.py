# Generated by Django 4.1.2 on 2022-12-10 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_delete_blog_delete_internship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phonenumber',
        ),
    ]
