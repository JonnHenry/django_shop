# Generated by Django 3.1 on 2021-03-30 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210326_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.CharField(default='https://firebasestorage.googleapis.com/v0/b/e-commerce-19b59.appspot.com/o/default%2Fdefault.jpg?alt=media&token=90f710d3-1d62-4e4a-87b1-506a3b9c042a', max_length=300, unique=True, verbose_name='Imagen principal'),
        ),
        migrations.AlterField(
            model_name='product',
            name='secondary_image',
            field=models.CharField(default='https://firebasestorage.googleapis.com/v0/b/e-commerce-19b59.appspot.com/o/default%2Fdefault.jpg?alt=media&token=90f710d3-1d62-4e4a-87b1-506a3b9c042a', max_length=300, unique=True, verbose_name='Imagen principal'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thirth_image',
            field=models.CharField(default='https://firebasestorage.googleapis.com/v0/b/e-commerce-19b59.appspot.com/o/default%2Fdefault.jpg?alt=media&token=90f710d3-1d62-4e4a-87b1-506a3b9c042a', max_length=300, unique=True, verbose_name='Imagen principal'),
        ),
    ]
