# Generated by Django 2.2 on 2019-04-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadmin', '0004_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='job',
            field=models.SmallIntegerField(choices=[(0, '员工'), (1, '仓库管理员'), (2, '主管'), (3, '经理')], default=0, verbose_name='工种'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.SmallIntegerField(choices=[(1, '男'), (0, '女')], default=1, verbose_name='性别'),
        ),
    ]
