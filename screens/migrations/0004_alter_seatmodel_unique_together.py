# Generated by Django 4.1.7 on 2023-04-02 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0003_alter_moviemodel_id_alter_screenmodel_id_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seatmodel',
            unique_together={('screen', 'column', 'row')},
        ),
    ]
