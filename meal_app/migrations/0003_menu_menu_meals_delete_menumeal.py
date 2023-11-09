# Generated by Django 4.2.7 on 2023-11-09 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_app', '0002_remove_menu_menu_meals_alter_menu_table_menumeal'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_meals',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='meal_app.meal'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MenuMeal',
        ),
    ]
