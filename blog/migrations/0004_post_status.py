# Generated by Django 2.0.8 on 2019-10-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191009_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
