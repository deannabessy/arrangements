# Generated by Django 3.2.12 on 2022-06-01 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tempFeedConsumer', '0003_rename_tempreading_reading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='temp',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]