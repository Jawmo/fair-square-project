# Generated by Django 4.0.5 on 2022-06-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_emails', '0007_emailversion_created_date_emailversion_modified_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailversion',
            name='email_name',
            field=models.CharField(default='name', max_length=50),
            preserve_default=False,
        ),
    ]
