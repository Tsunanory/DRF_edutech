# Generated by Django 5.0.6 on 2024-06-01 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ('-date',), 'verbose_name': 'оплата', 'verbose_name_plural': 'оплаты'},
        ),
    ]
