# Generated by Django 4.0.6 on 2022-08-09 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_alter_book_oblojka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.CharField(max_length=15),
        ),
    ]
