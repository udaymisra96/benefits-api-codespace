# Generated by Django 4.0.5 on 2022-07-14 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('screener', '0011_expense_household_member_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='householdmember',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='household_members', to='screener.screen'),
        ),
        migrations.AlterField(
            model_name='incomestream',
            name='household_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_streams', to='screener.householdmember'),
        ),
        migrations.AlterField(
            model_name='incomestream',
            name='screen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_streams', to='screener.screen'),
        ),
    ]
