# Generated by Django 3.2.7 on 2021-09-19 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_document_docfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
