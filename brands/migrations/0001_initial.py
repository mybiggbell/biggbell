# Generated by Django 4.1.6 on 2023-02-05 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=350)),
                ('detail_about_project', models.TextField()),
                ('total_cost', models.BigIntegerField()),
                ('project_file', models.FileField(upload_to='project_file')),
                ('project_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='userauth.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_note', models.TextField()),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='project_approval_user', to='userauth.creator')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_approval', to='brands.project')),
            ],
        ),
    ]
