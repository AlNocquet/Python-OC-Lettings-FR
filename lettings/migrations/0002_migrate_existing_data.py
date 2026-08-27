"""Database migration for lettings."""

from django.db import migrations


def copy_existing_data(apps, schema_editor):
    """Copy existing data into the refactored application."""
    db_alias = schema_editor.connection.alias

    LegacyAddress = apps.get_model('oc_lettings_site', 'Address')
    LegacyLetting = apps.get_model('oc_lettings_site', 'Letting')
    Address = apps.get_model('lettings', 'Address')
    Letting = apps.get_model('lettings', 'Letting')

    for legacy_address in LegacyAddress.objects.using(db_alias).all():
        Address.objects.using(db_alias).create(
            id=legacy_address.id,
            number=legacy_address.number,
            street=legacy_address.street,
            city=legacy_address.city,
            state=legacy_address.state,
            zip_code=legacy_address.zip_code,
            country_iso_code=legacy_address.country_iso_code,
        )

    for legacy_letting in LegacyLetting.objects.using(db_alias).all():
        Letting.objects.using(db_alias).create(
            id=legacy_letting.id,
            title=legacy_letting.title,
            address_id=legacy_letting.address_id,
        )


def reverse_existing_data(apps, schema_editor):
    """Remove data copied by the forward migration."""
    db_alias = schema_editor.connection.alias

    LegacyAddress = apps.get_model('oc_lettings_site', 'Address')
    LegacyLetting = apps.get_model('oc_lettings_site', 'Letting')
    Address = apps.get_model('lettings', 'Address')
    Letting = apps.get_model('lettings', 'Letting')

    legacy_letting_ids = LegacyLetting.objects.using(
        db_alias
    ).values_list('id', flat=True)

    legacy_address_ids = LegacyAddress.objects.using(
        db_alias
    ).values_list('id', flat=True)

    Letting.objects.using(db_alias).filter(
        id__in=legacy_letting_ids
    ).delete()

    Address.objects.using(db_alias).filter(
        id__in=legacy_address_ids
    ).delete()


class Migration(migrations.Migration):
    """Define the operations for this database migration."""

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_existing_data,
            reverse_existing_data,
        ),
    ]
