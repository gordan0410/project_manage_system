# Generated by Django 3.1.4 on 2021-05-28 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pms_index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='owner',
        ),
        migrations.AddField(
            model_name='projectmembers',
            name='owner',
            field=models.CharField(default='root', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectmembers',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.CharField(default='active', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='projectmembers',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='projectmembers',
            name='member_id',
        ),
        migrations.AddField(
            model_name='projectmembers',
            name='member_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectmembers',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pms_index.projects'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
