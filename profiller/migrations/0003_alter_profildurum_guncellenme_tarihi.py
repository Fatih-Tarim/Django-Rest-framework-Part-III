# Generated by Django 4.2.1 on 2023-05-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiller", "0002_alter_profil_options_alter_profildurum_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profildurum",
            name="guncellenme_tarihi",
            field=models.DateTimeField(null=True),
        ),
    ]
