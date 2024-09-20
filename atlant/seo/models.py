from django.db import models


class CompanyModel(models.Model):
    phone = models.CharField(max_length=25, 
                             verbose_name='Номер телефона',
                             help_text='в формате +7(900)000-00-00')
    e_mail = models.CharField(max_length=200,
                               verbose_name='Адрес электронной почты')
    vk = models.CharField(max_length=200,
                               verbose_name='ВКонтакте',
                               help_text='ссылка на сообщество в ВК')
    whatsapp = models.CharField(max_length=200,
                               verbose_name='Вацап',
                               help_text='Ссылка на вацап (формируется на специальных сервисах)')
    telegramm = models.CharField(max_length=200,
                               verbose_name='Телеграмм',
                               help_text='Ссылка на телеграмм канал')
    address = models.CharField(max_length=200,
                               verbose_name='Фактический адрес',
                               help_text='!Внимание! адрес изменится только в подвале сайта')
    
    def __str__(self):

        return self.address

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Адрес и контакты организации'



class SEOModel(models.Model):
    title = models.CharField(max_length=50, 
                             verbose_name='Имя страницы',
                             help_text='Влияет на поисковую выдачу, Уникальное имя должно быть. Не больше 50 символов')
    description = models.CharField(max_length=200,
                               verbose_name='Описание старницы.',
                               help_text='Не больше 200 символов. Важный элемент поисковой индексации. Должен быть связный текст, по нему поисковые роботы индексируют сайт')
    keywords = models.CharField(max_length=250,
                               verbose_name='Ключевые слова',
                               help_text='Указываетя через запятую. Не больше 250 символов. Устаревший элемент, не влияет на поисковую выдачу. Но учавствует в формировании семантического ядра')

    def __str__(self):

        return self.title

    class Meta:
        verbose_name = 'SEO'
        verbose_name_plural = 'Информация для поисковых систем'



class FirstPageNews(models.Model):
    title = models.CharField(max_length=150, 
                             verbose_name='Название',
                             help_text='Влияет на поисковую выдачу, Уникальное имя должно быть. Не больше 50 символов')
    description = models.CharField(max_length=200,
                               verbose_name='Текст',
                               help_text='Не больше 200 символов. Важный элемент поисковой индексации. Должен быть связный текст, по нему поисковые роботы индексируют сайт')
    def __str__(self):

        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости первой страницы'

