# Generated by Django 4.0.5 on 2022-06-07 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction_emails', '0008_emailversion_email_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailversion',
            options={'ordering': ['-created_date'], 'verbose_name': 'Email Version'},
        ),
        migrations.AlterModelOptions(
            name='transactionemail',
            options={'ordering': ['-created_date'], 'verbose_name': 'Transaction Email'},
        ),
        migrations.RenameField(
            model_name='emailversion',
            old_name='version',
            new_name='version_alias',
        ),
    ]
