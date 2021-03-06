# Generated by Django 2.2 on 2020-03-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_contactinfo_message_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='message_content',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='message_type',
            field=models.CharField(choices=[('general', 'General Interest'), ('project', 'Project Offer'), ('bug', 'Bug Report')], max_length=128, verbose_name='What is this regarding?'),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Name'),
        ),
    ]
