# Generated by Django 2.2.4 on 2019-08-21 05:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Company title')),
                ('address', models.CharField(max_length=255, verbose_name='Company address')),
                ('number_of_employees_from', models.IntegerField(default=1, verbose_name='Number of employees from')),
                ('number_of_employees_to', models.IntegerField(default=1, verbose_name='Number of employees to')),
                ('description', models.TextField(verbose_name='Company description')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone number')),
                ('fax', models.CharField(blank=True, max_length=32, null=True, verbose_name='Fax number')),
                ('url', models.URLField(blank=True, max_length=255, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='JobField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Job field')),
                ('position', models.IntegerField(verbose_name='Sort order')),
            ],
            options={
                'verbose_name': 'Job field',
                'verbose_name_plural': 'Job fields',
            },
        ),
        migrations.CreateModel(
            name='JobOpenings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Job opening title')),
                ('description', models.TextField(verbose_name='Job description')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('language', models.CharField(choices=[('th', 'Thai'), ('en', 'English'), ('ko', 'Korean'), ('cn', 'Chinese'), ('ja', 'Japanese')], default='th', max_length=2)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], db_index=True, default=0, verbose_name='Status')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.Company', verbose_name='Company')),
                ('job_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.JobField', verbose_name='Job field')),
            ],
            options={
                'verbose_name': 'Job opening',
                'verbose_name_plural': 'Job openings',
            },
        ),
    ]
