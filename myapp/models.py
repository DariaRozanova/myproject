from django.db import models
import pandas as pd
# Create your models here.
class GeographyPage(models.Model):
    chart_first = models.ImageField(upload_to='images', blank=True, verbose_name="1.0 Город/зарплата (общая)")
    table_first = models.FileField(upload_to='uploads/', blank=True, verbose_name="1.1 Город/зарплата (общая) таблица")

    chart_second = models.ImageField(upload_to='images', blank=True, verbose_name="2.0 Город/доля (общая)")
    table_second = models.FileField(upload_to='uploads/', blank=True, verbose_name="2.1 Город/доля (общая) таблица")

    chart_third = models.ImageField(upload_to='images', blank=True, verbose_name="3.0 Город/зарплата (для профессии)")
    table_third = models.FileField(upload_to='uploads/', blank=True, verbose_name="3.1 Город/зарплата (для профессии) таблица")

    chart_fourth = models.ImageField(upload_to='images', blank=True, verbose_name="4.0 Город/доля (для профессии)")
    table_fourth = models.FileField(upload_to='uploads/', blank=True, verbose_name="4.1 Город/доля (для профессии) таблица")

class DemandPage(models.Model):
    chart_first = models.ImageField(upload_to='images', verbose_name="1.0 Год/зарплата (общая)")
    chart_second = models.ImageField(upload_to='images', verbose_name="1.1 Год/количество (общая)")
    table_all = models.FileField(upload_to='uploads/',blank=True, verbose_name="1.3 Год/зарплата/количество (общая) таблица")

    chart_third = models.ImageField(upload_to='images', verbose_name="3.0 Год/зарплата (для профессии)")
    chart_fourth = models.ImageField(upload_to='images', verbose_name="4.0 Год/количество (для профессии)")
    table_vac = models.FileField(upload_to='uploads/', blank=True, verbose_name="4.1 Год/зарплата/количество (для профессии) таблица")

class SkillsPage(models.Model):
    chart_0_1 = models.ImageField(upload_to='images', verbose_name="Навыки 2015 (общее)")
    chart_0_2 = models.ImageField(upload_to='images', verbose_name="Навыки 2016 (общее)")
    chart_0_3 = models.ImageField(upload_to='images', verbose_name="Навыки 2017 (общее)")
    chart_0_4 = models.ImageField(upload_to='images', verbose_name="Навыки 2018 (общее)")
    chart_0_5 = models.ImageField(upload_to='images', verbose_name="Навыки 2019 (общее)")
    chart_0_6 = models.ImageField(upload_to='images', verbose_name="Навыки 2020 (общее)")
    chart_0_7 = models.ImageField(upload_to='images', verbose_name="Навыки 2021 (общее)")
    chart_0_8 = models.ImageField(upload_to='images', verbose_name="Навыки 2022 (общее)")
    chart_0_9 = models.ImageField(upload_to='images', verbose_name="Навыки 2023 (общее)")
    table_0_1 = models.FileField(upload_to='uploads/', verbose_name="Таблица (общее)")

    chart_1_1 = models.ImageField(upload_to='images', verbose_name="Навыки 2015 (профессия)")
    chart_1_2 = models.ImageField(upload_to='images', verbose_name="Навыки 2016 (профессия)")
    chart_1_3 = models.ImageField(upload_to='images', verbose_name="Навыки 2017 (профессия)")
    chart_1_4 = models.ImageField(upload_to='images', verbose_name="Навыки 2018 (профессия)")
    chart_1_5 = models.ImageField(upload_to='images', verbose_name="Навыки 2019 (профессия)")
    chart_1_6 = models.ImageField(upload_to='images', verbose_name="Навыки 2020 (профессия)")
    chart_1_7 = models.ImageField(upload_to='images', verbose_name="Навыки 2021 (профессия)")
    chart_1_8 = models.ImageField(upload_to='images', verbose_name="Навыки 2022 (профессия)")
    chart_1_9 = models.ImageField(upload_to='images', verbose_name="Навыки 2023 (профессия)")
    table_1_1 = models.FileField(upload_to='uploads/', verbose_name="Таблица (профессия)")

class MainPage(models.Model):
    text = models.TextField(verbose_name="Текст")

