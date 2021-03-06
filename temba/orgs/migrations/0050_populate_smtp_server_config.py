# Generated by Django 2.0.8 on 2018-10-22 13:44

from urllib.parse import quote, urlencode

from django.db import migrations


def populate_smtp_server_config(apps, schema_editor):
    Org = apps.get_model("orgs", "Org")

    orgs = Org.objects.filter(config__icontains="smtp")
    for org in orgs:
        config = org.config

        smtp_from_email = config.get("SMTP_FROM_EMAIL", "")
        smtp_host = config.get("SMTP_HOST", "")
        smtp_username = config.get("SMTP_USERNAME", "")
        smtp_password = config.get("SMTP_PASSWORD", "")
        smtp_port = config.get("SMTP_PORT", "")
        use_tls = config.get("SMTP_ENCRYPTION", "") == "T"

        if not smtp_host:
            continue

        query = urlencode({"from": smtp_from_email, "tls": str(use_tls).lower()})
        url = f"smtp://{quote(smtp_username)}:{quote(smtp_password)}@{smtp_host}:{smtp_port}/?{query}"
        org.config["smtp_server"] = url

        # clear out old keys
        for key in ("SMTP_ENCRYPTION", "SMTP_FROM_EMAIL", "SMTP_HOST", "SMTP_PORT", "SMTP_USERNAME", "SMTP_PASSWORD"):
            if key in org.config:
                del org.config[key]

        org.save(update_fields=("config",))


class Migration(migrations.Migration):

    dependencies = [("orgs", "0049_org_flow_server_enabled")]

    operations = [migrations.RunPython(populate_smtp_server_config)]
