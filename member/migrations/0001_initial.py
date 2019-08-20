# Generated by Django 2.2.4 on 2019-08-20 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailBanned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
            ],
            options={
                'verbose_name': 'Banned Email Address',
                'verbose_name_plural': 'Banned Email Addresses',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('resume_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('title', models.CharField(max_length=255, verbose_name='Resume title')),
                ('description', models.TextField(verbose_name='Resume description')),
                ('primary', models.BooleanField(db_index=True, default=False, verbose_name='Primary resume')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], db_index=True, default=0, verbose_name='Status')),
                ('language', models.IntegerField(choices=[(0, 'Thai'), (1, 'English'), (2, 'Korean'), (3, 'Chinese'), (4, 'Japanese')], db_index=True, default=0, verbose_name='Language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resume',
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('present', models.BooleanField(db_index=True, default=False, verbose_name='Present')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('company', models.CharField(max_length=255, verbose_name='Company')),
                ('title', models.CharField(max_length=255, verbose_name='Job title')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Resume', verbose_name='Resume')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('organization', models.CharField(blank=True, max_length=255, verbose_name='Organization')),
                ('status_memo', models.CharField(blank=True, max_length=255, verbose_name='User status memo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='LoginLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP address')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_loginlog_owned', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Login log',
                'verbose_name_plural': 'Login logs',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.URLField(max_length=255, verbose_name='URL')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Resume', verbose_name='Resume')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('present', models.BooleanField(db_index=True, default=False, verbose_name='Present')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('school', models.CharField(max_length=255, verbose_name='School')),
                ('degree', models.CharField(max_length=255, verbose_name='Degree')),
                ('major', models.CharField(max_length=255, verbose_name='Major')),
                ('topic', models.TextField(verbose_name='Research topics')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Resume', verbose_name='Resume')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
