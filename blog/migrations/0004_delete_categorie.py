# Generated by Django 3.0 on 2020-08-20 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_article_categorie'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categorie',
        ),
    ]
