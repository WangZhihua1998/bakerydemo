# Generated by Django 2.1.9 on 2019-07-24 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize", "0002_initial_data"),
        ("wagtailimages", "0001_squashed_0021"),
        ("locations", "0006_wagtail_localize_3"),
    ]

    # operations = [
    #     migrations.CreateModel(
    #         name='RegionFlag',
    #         fields=[
    #             ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
    #             ('flag_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
    #             ('region', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='flag', to='wagtail_localize.Region')),
    #         ],
    #     ),
    # ]