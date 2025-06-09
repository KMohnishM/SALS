from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_add_all_concepts'),
    ]

    operations = [
        migrations.AddField(
            model_name='learningpath',
            name='all_concepts',
            field=models.JSONField(blank=True, null=True),
        ),
    ] 