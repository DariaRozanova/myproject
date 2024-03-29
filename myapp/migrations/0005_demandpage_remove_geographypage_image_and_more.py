# Generated by Django 5.0.1 on 2024-01-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_geographypage_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemandPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart_first', models.ImageField(upload_to='images', verbose_name='1.0 Год/зарплата (общая)')),
                ('table_first', models.FileField(upload_to='uploads/', verbose_name='1.1 Год/зарплата (общая) таблица')),
                ('chart_second', models.ImageField(upload_to='images', verbose_name='2.0 Год/количество (общая)')),
                ('table_second', models.FileField(upload_to='uploads/', verbose_name='2.1 Год/количество (общая) таблица')),
                ('chart_third', models.ImageField(upload_to='images', verbose_name='3.0 Год/зарплата (для профессии)')),
                ('table_third', models.FileField(upload_to='uploads/', verbose_name='3.1 Год/зарплата (для профессии) таблица')),
                ('chart_fourth', models.ImageField(upload_to='images', verbose_name='4.0 Год/количество (для профессии)')),
                ('table_fourth', models.FileField(upload_to='uploads/', verbose_name='4.1 Год/количество (для профессии) таблица')),
            ],
        ),
        migrations.RemoveField(
            model_name='geographypage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='geographypage',
            name='table',
        ),
        migrations.AddField(
            model_name='geographypage',
            name='chart_first',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='1.0 Город/зарплата (общая)'),
        ),
        migrations.AddField(
            model_name='geographypage',
            name='chart_fourth',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='4.0 Город/доля (для профессии)'),
        ),
        migrations.AddField(
            model_name='geographypage',
            name='chart_second',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='2.0 Город/доля (общая)'),
        ),
        migrations.AddField(
            model_name='geographypage',
            name='chart_third',
            field=models.ImageField(blank=True, upload_to='images', verbose_name='3.0 Город/зарплата (для профессии)'),
        ),
        migrations.AddField(
            model_name='geographypage',
            name='table_first',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='1.1 Город/зарплата (общая) таблица'),
        ),
        migrations.AddField(
            model_name='geographypage',
            name='table_fourth',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='4.1 Город/доля (для профессии) таблица'),
        ),
        migrations.AddField(
            model_name='geographypage',
            name='table_second',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='2.1 Город/доля (общая) таблица'),
        ),
        migrations.AddField(
            model_name='geographypage',
            name='table_third',
            field=models.FileField(blank=True, upload_to='uploads/', verbose_name='3.1 Город/зарплата (для профессии) таблица'),
        ),
    ]
