from django.db import migrations


def copy_existing_data(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    LegacyProfile = apps.get_model('oc_lettings_site', 'Profile')
    Profile = apps.get_model('profiles', 'Profile')

    for legacy_profile in LegacyProfile.objects.using(db_alias).all():
        Profile.objects.using(db_alias).create(
            id=legacy_profile.id,
            user_id=legacy_profile.user_id,
            favorite_city=legacy_profile.favorite_city,
        )


def reverse_existing_data(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    LegacyProfile = apps.get_model('oc_lettings_site', 'Profile')
    Profile = apps.get_model('profiles', 'Profile')

    legacy_profile_ids = LegacyProfile.objects.using(
        db_alias
    ).values_list('id', flat=True)

    Profile.objects.using(db_alias).filter(
        id__in=legacy_profile_ids
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            copy_existing_data,
            reverse_existing_data,
        ),
    ]
