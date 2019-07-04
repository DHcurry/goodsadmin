# Generated by Django 2.2 on 2019-04-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadmin', '0003_remove_user_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.SmallIntegerField(choices=[(1, '男'), (0, '女')], default=1, verbose_name='性别'),
            preserve_default=False,
        ),
    ]
