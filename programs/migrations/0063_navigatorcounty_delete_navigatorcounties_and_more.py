# Generated by Django 4.2.6 on 2024-01-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0062_navigatorcounties_navigator_counties"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavigatorCounty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name="NavigatorCounties",
        ),
        migrations.AlterField(
            model_name="navigator",
            name="counties",
            field=models.ManyToManyField(
                blank=True, related_name="navigator", to="programs.navigatorcounty"
            ),
        ),
    ]
