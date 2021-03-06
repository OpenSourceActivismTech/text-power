# Generated by Django 2.1.5 on 2019-02-04 19:44

from django.db import migrations


def remove_test_contacts(apps, schema_editor):
    ChannelConnection = apps.get_model("channels", "ChannelConnection")
    ChannelEvent = apps.get_model("channels", "ChannelEvent")
    Contact = apps.get_model("contacts", "Contact")
    BroadcastRecipient = apps.get_model("msgs", "BroadcastRecipient")

    num_deleted = 0
    for test_contact in Contact.objects.filter(is_test=True):
        BroadcastRecipient.objects.filter(contact=test_contact).delete()

        test_contact.msgs.all().update(response_to=None)
        test_contact.msgs.all().delete()

        test_contact.webhook_results.all().delete()

        for test_run in test_contact.runs.order_by("-id"):
            test_run.webhook_events.all().delete()
            test_run.logs.all().delete()
            test_run.delete()

        ChannelConnection.objects.filter(contact=test_contact).delete()
        ChannelEvent.objects.filter(contact=test_contact).delete()

        test_contact.urns.all().delete()

        test_contact.delete()
        num_deleted += 1

    if num_deleted:
        print(f"Deleted {num_deleted} test contacts")


def unremove_test_contacts(apps, schema_editor):
    pass


def apply_manual():
    from django.apps import apps

    remove_test_contacts(apps, None)


class Migration(migrations.Migration):

    dependencies = [("contacts", "0093_auto_20190131_1116")]

    operations = [migrations.RunPython(remove_test_contacts, unremove_test_contacts)]
