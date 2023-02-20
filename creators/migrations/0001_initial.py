# Generated by Django 4.1.6 on 2023-02-18 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0003_alter_brand_profile_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatorInbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('file', models.FileField(default=None, upload_to='creatorInbox')),
                ('description', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatorInbox', to='userauth.brand')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creatorInbox', to='userauth.creator')),
            ],
        ),
    ]
