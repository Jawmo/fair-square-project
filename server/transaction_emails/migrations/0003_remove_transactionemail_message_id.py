# Generated by Django 4.0.5 on 2022-06-06 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_emails', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionemail',
            name='message_id',
        ),
    ]
