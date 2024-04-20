# Generated by Django 4.2.6 on 2024-04-20 21:25

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("translations", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
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
                (
                    "external_name",
                    models.CharField(
                        blank=True, max_length=120, null=True, unique=True
                    ),
                ),
                (
                    "text",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="documents",
                        to="translations.translation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FederalPoveryLimit",
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
                ("year", models.CharField(max_length=32, unique=True)),
                ("has_1_person", models.IntegerField()),
                ("has_2_people", models.IntegerField()),
                ("has_3_people", models.IntegerField()),
                ("has_4_people", models.IntegerField()),
                ("has_5_people", models.IntegerField()),
                ("has_6_people", models.IntegerField()),
                ("has_7_people", models.IntegerField()),
                ("has_8_people", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="LegalStatus",
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
                ("status", models.CharField(max_length=256)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="programs.legalstatus",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Navigator",
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
                (
                    "external_name",
                    models.CharField(
                        blank=True, max_length=120, null=True, unique=True
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                (
                    "assistance_link",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="navigator_assistance_link",
                        to="translations.translation",
                    ),
                ),
            ],
        ),
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
        migrations.CreateModel(
            name="Program",
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
                ("name_abbreviated", models.CharField(max_length=120)),
                (
                    "external_name",
                    models.CharField(
                        blank=True, max_length=120, null=True, unique=True
                    ),
                ),
                ("active", models.BooleanField(blank=True, default=True)),
                ("low_confidence", models.BooleanField(blank=True, default=False)),
                (
                    "apply_button_link",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_apply_button_link",
                        to="translations.translation",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_category",
                        to="translations.translation",
                    ),
                ),
                (
                    "description",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_description",
                        to="translations.translation",
                    ),
                ),
                (
                    "description_short",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_description_short",
                        to="translations.translation",
                    ),
                ),
                (
                    "documents",
                    models.ManyToManyField(
                        blank=True,
                        related_name="program_documents",
                        to="programs.document",
                    ),
                ),
                (
                    "estimated_application_time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_estimated_application_time",
                        to="translations.translation",
                    ),
                ),
                (
                    "estimated_delivery_time",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_estimated_delivery_time",
                        to="translations.translation",
                    ),
                ),
                (
                    "fpl",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="fpl",
                        to="programs.federalpoverylimit",
                    ),
                ),
                (
                    "learn_more_link",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_learn_more_link",
                        to="translations.translation",
                    ),
                ),
                (
                    "legal_status_required",
                    models.ManyToManyField(
                        blank=True, related_name="programs", to="programs.legalstatus"
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_name",
                        to="translations.translation",
                    ),
                ),
                (
                    "value_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_value_type",
                        to="translations.translation",
                    ),
                ),
                (
                    "warning",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="program_warning",
                        to="translations.translation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UrgentNeedCategory",
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
                ("name", models.CharField(max_length=120)),
            ],
            options={
                "verbose_name_plural": "Urgent Need Categories",
            },
        ),
        migrations.CreateModel(
            name="UrgentNeedFunction",
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
                ("name", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="WebHookFunction",
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
        migrations.CreateModel(
            name="UrgentNeed",
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
                (
                    "external_name",
                    models.CharField(
                        blank=True, max_length=120, null=True, unique=True
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("active", models.BooleanField(blank=True, default=True)),
                ("low_confidence", models.BooleanField(blank=True, default=False)),
                (
                    "description",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urgent_need_description",
                        to="translations.translation",
                    ),
                ),
                (
                    "functions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="function",
                        to="programs.urgentneedfunction",
                    ),
                ),
                (
                    "link",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urgent_need_link",
                        to="translations.translation",
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urgent_need_name",
                        to="translations.translation",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urgent_need_type",
                        to="translations.translation",
                    ),
                ),
                (
                    "type_short",
                    models.ManyToManyField(
                        related_name="urgent_needs", to="programs.urgentneedcategory"
                    ),
                ),
                (
                    "warning",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="urgent_need_warning",
                        to="translations.translation",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Referrer",
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
                ("referrer_code", models.CharField(max_length=64, unique=True)),
                (
                    "webhook_url",
                    models.CharField(blank=True, max_length=320, null=True),
                ),
                (
                    "primary_navigators",
                    models.ManyToManyField(
                        blank=True,
                        related_name="primary_navigators",
                        to="programs.navigator",
                    ),
                ),
                (
                    "remove_programs",
                    models.ManyToManyField(
                        blank=True,
                        related_name="removed_programs",
                        to="programs.program",
                    ),
                ),
                (
                    "webhook_functions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="web_hook",
                        to="programs.webhookfunction",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="navigator",
            name="counties",
            field=models.ManyToManyField(
                blank=True, related_name="navigator", to="programs.navigatorcounty"
            ),
        ),
        migrations.AddField(
            model_name="navigator",
            name="description",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="navigator_name_description",
                to="translations.translation",
            ),
        ),
        migrations.AddField(
            model_name="navigator",
            name="email",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="navigator_email",
                to="translations.translation",
            ),
        ),
        migrations.AddField(
            model_name="navigator",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="navigator_name",
                to="translations.translation",
            ),
        ),
        migrations.AddField(
            model_name="navigator",
            name="program",
            field=models.ManyToManyField(
                blank=True, related_name="navigator", to="programs.program"
            ),
        ),
    ]
