# Generated by Django 3.2.4 on 2021-06-24 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20210622_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='food',
        ),
        migrations.AddField(
            model_name='product',
            name='have_food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='tracker.food'),
        ),
        migrations.AddField(
            model_name='product',
            name='have_recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='have_recipe', to='tracker.recipe'),
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.FloatField(verbose_name='Food calories in 100 gram'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belong_to_recipe', to='tracker.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.recipe', verbose_name='Eaten food'),
        ),
        migrations.AlterField(
            model_name='record',
            name='weight',
            field=models.FloatField(verbose_name='Weight of eaten food'),
        ),
    ]
