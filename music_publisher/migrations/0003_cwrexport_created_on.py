# Generated by Django 3.2.6 on 2021-08-16 15:15

from django.db import migrations, models
from django.utils.timezone import datetime, make_aware, get_fixed_timezone


def set_created_on(apps, schema_editor):
    cls = apps.get_model('music_publisher', 'CWRExport')
    qs = cls.objects.filter(created_on__isnull=True)
    for obj in qs:
        if obj.nwr_rev in ['NWR', 'NW2', 'REV', 'RE2']:
            s = obj.cwr[64:78]
        else:
            s = obj.cwr[65:79]
        obj.created_on = make_aware(
            datetime.strptime(s, '%Y%m%d%H%M%S'), get_fixed_timezone(0)
        )
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('music_publisher', '0002_mayday'),
    ]

    operations = [
        migrations.AddField(
            model_name='cwrexport',
            name='created_on',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.RunPython(
            code=set_created_on,
            reverse_code=migrations.operations.special.RunPython.noop,
        ),
    ]
