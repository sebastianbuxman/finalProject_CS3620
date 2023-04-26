# Generated by Django 3.2 on 2023-04-24 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesimulatte', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='image',
            field=models.ImageField(default='images/none/noimg.jpg', upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
