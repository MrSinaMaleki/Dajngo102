# Generated by Django 5.1 on 2024-08-11 20:17

import post.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_created_at_alter_post_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img_field',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=64, validators=[post.validators.author_name_valid], verbose_name='author name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=1024, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=64, validators=[post.validators.len_min], verbose_name='title'),
        ),
    ]
