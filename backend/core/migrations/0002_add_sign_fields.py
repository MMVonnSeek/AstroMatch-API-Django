from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='date_start',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='sign',
            name='date_end',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='sign',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
