import apps.manager.models.image
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('value', models.TextField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Created date of the tag', verbose_name='Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ImageField(help_text='Image', unique=True, upload_to=apps.manager.models.image.name_file, verbose_name='Content')),
                ('metadata', models.JSONField(blank=True, help_text='Metadata of the image', null=True, verbose_name='Metadata')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Created date of the image', verbose_name='Date')),
                ('tags', models.ManyToManyField(blank=True, default=None, help_text='Tags for the image', related_name='images', related_query_name='image', to='manager.Tag', verbose_name='Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
