# Generated by Django 3.2.4 on 2021-06-24 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20210624_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belong_recipe', to='tracker.recipe'),
        ),
    ]
