# Generated by Django 2.1.8 on 2019-06-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flows", "0200_backfill_flow_deps")]

    operations = [
        migrations.AlterField(model_name="flow", name="flow_server_enabled", field=models.BooleanField(default=True))
    ]
