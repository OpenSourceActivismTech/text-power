# Generated by Django 2.1.3 on 2019-01-16 17:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("channels", "0112_auto_20190111_1718"), ("flows", "0191_add_deps_for_start_new_flow_action")]

    operations = [
        migrations.AddField(
            model_name="flowstart",
            name="connections",
            field=models.ManyToManyField(
                help_text="The channel connections created for this start",
                related_name="starts",
                to="channels.ChannelConnection",
            ),
        ),
        migrations.AlterField(
            model_name="flowstart",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="flows_flowstart_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="flowstart",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="flows_flowstart_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
