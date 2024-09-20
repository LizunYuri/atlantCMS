from django.utils import timezone
import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class ScheduleModel(models.Model):
    class Weekday(models.IntegerChoices):
        MONDAY = 1, _('Понедельник')
        TUESDAY = 2, _('Вторник')
        WEDNESDAY = 3, _('Среда')
        THURSDAY = 4, _('Четверг')
        FRIDAY = 5, _('Пятница')
        SATURDAY = 6, _('Суббота')
        SUNDAY = 7, _('Воскресенье')

    weekday = models.IntegerField(choices=Weekday.choices, verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Начало",
                                  help_text='в формате ЧЧ:ММ')
    end_time = models.TimeField(verbose_name="Конец",
                                help_text='в формате ЧЧ:ММ')
    age = models.CharField(max_length=30, verbose_name="Возрастая группа")

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['weekday', 'start_time']

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Время окончания должно быть больше времени начала.')


    def __str__(self):
        return f'{self.get_weekday_display()} - с {self.start_time} до {self.end_time} (Возраст: {self.age})'


class ClientModel(models.Model):
    name = models.CharField(max_length=100,
                             verbose_name='Имя',
                             help_text='Не больше 100 символов')
    phone = models.CharField(max_length=170,
                                verbose_name='номер телефона',
                                help_text='Не больше 70 символов, обязательно к заполнению, используется для поисковой индексации',
                                null=True)
    email = models.EmailField(
                                verbose_name='Адрес электронной почты',
                                help_text='Не больше 70 символов, обязательно к заполнению, используется для поисковой индексации',
                                null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиенты с сайта'
        verbose_name_plural = 'Клиенты с сайта'
