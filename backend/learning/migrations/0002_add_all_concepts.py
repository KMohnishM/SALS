from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquizattempt',
            name='all_concepts',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userquizattempt',
            name='user_answers',
            field=models.JSONField(blank=True, null=True),
        ),
    ] 