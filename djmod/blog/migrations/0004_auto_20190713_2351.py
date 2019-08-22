# Generated by Django 2.2.3 on 2019-07-13 23:51

import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_postmodel_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[blog.validators.validate_author_email, blog.validators.validate_justin]),
        ),
    ]
