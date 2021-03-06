# Generated by Django 2.0.8 on 2018-08-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("triggers", "0012_initial")]

    operations = [
        migrations.AlterField(
            model_name="trigger",
            name="trigger_type",
            field=models.CharField(
                choices=[
                    ("K", "Keyword Trigger"),
                    ("S", "Schedule Trigger"),
                    ("V", "Inbound Call Trigger"),
                    ("M", "Missed Call Trigger"),
                    ("C", "Catch All Trigger"),
                    ("N", "New Conversation Trigger"),
                    ("U", "USSD Pull Session Trigger"),
                    ("R", "Referral Trigger"),
                ],
                default="K",
                help_text="The type of this trigger",
                max_length=1,
                verbose_name="Trigger Type",
            ),
        )
    ]
