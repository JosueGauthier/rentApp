# Generated by Django 4.1.3 on 2022-11-25 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("organization", "0003_product_is_consumable"),
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="product_rented",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="organization.product",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="reservation",
            name="renter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
