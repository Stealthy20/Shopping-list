# Generated by Django 3.2.16 on 2022-11-14 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shopping_list', '0012_createshoppinglist'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CreateShoppingList',
        ),
    ]
