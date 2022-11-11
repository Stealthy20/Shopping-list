# Generated by Django 3.2.16 on 2022-11-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Categories',
            new_name='AddCategory',
        ),
        migrations.DeleteModel(
            name='ShopItem',
        ),
        migrations.AlterModelOptions(
            name='addcategory',
            options={'ordering': ['category']},
        ),
        migrations.RenameField(
            model_name='addcategory',
            old_name='category_name',
            new_name='category',
        ),
    ]
