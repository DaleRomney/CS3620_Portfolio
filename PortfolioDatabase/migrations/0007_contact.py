# Generated by Django 4.0.2 on 2022-02-25 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0006_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=200)),
                ('c_email', models.CharField(max_length=200)),
                ('c_message', models.CharField(default='Personal Message goes here.', max_length=500)),
            ],
        ),
    ]
