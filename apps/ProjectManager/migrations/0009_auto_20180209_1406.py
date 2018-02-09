# Generated by Django 2.0.2 on 2018-02-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0008_inceptionhostconfig_is_enable'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlineauditcontents',
            name='dst_database',
            field=models.CharField(default='', max_length=80, verbose_name='操作目标数据库'),
        ),
        migrations.AddField(
            model_name='onlineauditcontents',
            name='dst_host',
            field=models.CharField(default='', max_length=30, verbose_name='操作目标数据库主机'),
        ),
        migrations.AddField(
            model_name='onlineauditcontents',
            name='op_type',
            field=models.CharField(default='', max_length=100, verbose_name='审核类型，数据修改or表结构变更'),
        ),
    ]