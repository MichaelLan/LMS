# Generated by Django 2.2.10 on 2020-05-02 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='code',
            field=models.CharField(blank=True, default='TAC1814', max_length=7, verbose_name='Teacher code'),
        ),
    ]