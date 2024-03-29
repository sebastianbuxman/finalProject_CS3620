# Generated by Django 3.2 on 2023-04-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(default='images/none/noimg.jpg', upload_to='Images')),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='', max_length=500)),
                ('address', models.CharField(default='', max_length=500)),
                ('email', models.EmailField(default='', max_length=100)),
                ('pNumber', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
