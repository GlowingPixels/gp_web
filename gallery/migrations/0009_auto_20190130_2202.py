# Generated by Django 2.1.3 on 2019-01-30 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20190126_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='descriptions',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='tag',
        ),
        migrations.AddField(
            model_name='gallery',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='gallery.ImageCategory'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='label',
            field=models.CharField(help_text='Name of the image must be related to image attributes', max_length=100),
        ),
    ]
