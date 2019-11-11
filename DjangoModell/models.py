from django.db import models


class TypeGroupModel(models.Model):
    bigInteger = models.BigIntegerField(help_text='64-битное целочисленное')
    binary = models.BinaryField(help_text='Поля для хранения бинарных данных')
    decimal = models.DecimalField(max_digits=7, decimal_places=3,
                                  help_text='Десятичное число с фиксированной точностью')
    float = models.FloatField(max_length=80, help_text='Число с плавающей точкой представленное объектом float.')
    integer = models.IntegerField(help_text='Число. Значение от -2147483648 до 2147483647')
    positiveInteger = models.PositiveIntegerField(help_text='Как и поле IntegerField, должно быть от 0 до 2147483647.')
    positiveSmallInteger = models.PositiveSmallIntegerField(help_text='Принимает значения от 0 до 32767.')
    smallInteger = models.SmallIntegerField(help_text='Принимает значения от -32768 до 32767.')
    boolean = models.BooleanField(default=True, help_text='Поле хранящее значение true/false.')
    nullBoolean = models.NullBooleanField(help_text='Как и BooleanField, но принимает значение NULL.')
    char = models.CharField(max_length=150, help_text='Строковое поле для хранения коротких или длинных строк.')
    text = models.TextField()
    file = models.FileField(help_text='Поле для загрузки файла',)
    date = models.DateField(auto_now=True, help_text='Дата, представленная в виде объекта datetime.date Python')
    dateTime = models.DateTimeField(auto_now=True,
                                    help_text='Дата и время, представленные объектом datetime.datetime Python')
    duration = models.DurationField(help_text='Поля для хранения периодов времени')
    time = models.TimeField(auto_now=True, help_text='Время, представленное объектом datetime.time Python')
    email = models.EmailField(blank=True, max_length=250,
                              help_text='Поле CharField для хранения правильного email-адреса')
    genericIPAddress = models.GenericIPAddressField(protocol='both', unpack_ipv4=True,
                                                    help_text='Адрес IPv4 или IPv6 в виде строки '
                                                              '(например, 192.0.2.30 или 2a02:42fe::4)')
    Slug = models.SlugField(blank=True, max_length=20)
    URL = models.URLField(blank=True, max_length=200)
    UUID = models.UUIDField(blank=True)
    FilePath = models.FilePathField(blank=True, max_length=150, path='C:/images')
    Image = models.ImageField(blank=True, width_field=100, height_field=100)

    class Meta:
        verbose_name = "Тип Полей"
        verbose_name_plural = "Типы Полей"

