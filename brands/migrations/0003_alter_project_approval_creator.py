# Generated by Django 4.1.6 on 2023-02-10 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
        ('brands', '0002_project_approval_is_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_approval',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_approval_user', to='userauth.creator'),
        ),
    ]
