# Generated by Django 4.1.7 on 2023-04-08 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.category'),
        ),
    ]
