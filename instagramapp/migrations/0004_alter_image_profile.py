# Generated by Django 3.2.8 on 2021-10-19 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagramapp.profile'),
        ),
    ]
