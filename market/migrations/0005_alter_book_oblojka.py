# Generated by Django 4.0.6 on 2022-08-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='oblojka',
            field=models.ImageField(blank=True, null=True, upload_to='internet_shop/shop/media/'),
        ),
    ]