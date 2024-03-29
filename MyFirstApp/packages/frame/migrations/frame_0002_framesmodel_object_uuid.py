# Generated by Django 4.2.6 on 2023-12-31 06:20

from django.db import migrations, models
import uuid


def create_uuid(apps, schema_editor):
    frames = apps.get_model("dynamic_models", "framesmodel")
    for frame in frames.objects.all():
        frame.object_uuid = uuid.uuid4()
        frame.save()


class Migration(migrations.Migration):
    dependencies = [
        ("dynamic_models", "frame_0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="framesmodel",
            name="object_uuid",
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.RunPython(create_uuid),
        migrations.AlterField(
            model_name="framesmodel",
            name="object_uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
