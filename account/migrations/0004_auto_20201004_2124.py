# Generated by Django 3.1 on 2020-10-04 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201004_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='major',
            options={'verbose_name': 'رشته', 'verbose_name_plural': 'رشته ها'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'دانشگاه', 'verbose_name_plural': 'دانشگاه ها'},
        ),
        migrations.AlterField(
            model_name='consultant',
            name='identity_code',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, verbose_name='کد ملی'),
        ),
    ]