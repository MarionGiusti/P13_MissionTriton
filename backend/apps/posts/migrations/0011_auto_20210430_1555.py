# Generated by Django 3.1.7 on 2021-04-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20210430_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='seashell.png', null=True, upload_to='post_pics'),
        ),
    ]
