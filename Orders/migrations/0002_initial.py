# Generated by Django 5.1.6 on 2025-02-07 03:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Orders', '0001_initial'),
        ('Products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commandeproduit',
            name='commande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.commande'),
        ),
        migrations.AddField(
            model_name='commandeproduit',
            name='produit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.produit'),
        ),
        migrations.AddField(
            model_name='commande',
            name='produits',
            field=models.ManyToManyField(through='Orders.CommandeProduit', to='Products.produit'),
        ),
    ]
