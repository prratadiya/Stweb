# Generated by Django 2.0.3 on 2018-04-02 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('st_web', '0006_auto_20180330_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial_detail',
            name='tutorial',
            field=models.FileField(default=0, upload_to='documents/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foss',
            name='contributor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
