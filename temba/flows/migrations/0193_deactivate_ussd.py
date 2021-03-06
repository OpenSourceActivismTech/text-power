# Generated by Django 2.1.5 on 2019-01-23 16:11

from django.db import migrations


def deactivate_ussd_flows(apps, schema_editor):
    Flow = apps.get_model("flows", "Flow")

    num_deactivated = 0
    for flow in Flow.objects.filter(flow_type="U"):
        flow.events.update(is_active=False)
        flow.triggers.all().delete()

        flow.group_dependencies.clear()
        flow.flow_dependencies.clear()
        flow.field_dependencies.clear()

        flow.is_active = False
        flow.save(update_fields=("is_active",))
        num_deactivated += 1

    if num_deactivated:
        print(f"Deactivated {num_deactivated} USSD flows")


class Migration(migrations.Migration):

    dependencies = [("flows", "0192_auto_20190116_1758")]

    operations = [migrations.RunPython(deactivate_ussd_flows)]
