# Generated by Django 4.1.7 on 2023-04-02 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0004_alter_seatmodel_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='showsmodel',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
