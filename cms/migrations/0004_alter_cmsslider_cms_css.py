# Generated by Django 3.2.5 on 2022-03-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20220328_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS Класс'),
        ),
    ]