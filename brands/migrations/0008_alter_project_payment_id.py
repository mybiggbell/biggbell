# Generated by Django 4.1.6 on 2023-02-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0007_project_paid_project_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='payment_id',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
