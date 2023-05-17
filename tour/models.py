from django.db import models


class TourAdd(models.Model):
    name = models.CharField(max_length=100)
    tour_time = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    price = models.IntegerField()
    when_is_tour = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/static/images/tour_images')
    image_2 = models.ImageField(upload_to='media/static/images/tour_images', blank=True, null=True)
    image_3 = models.ImageField(upload_to='media/static/images/tour_images', blank=True, null=True)
    image_4 = models.ImageField(upload_to='media/static/images/tour_images', blank=True, null=True)
    image_5 = models.ImageField(upload_to='media/static/images/tour_images', blank=True, null=True)
    image_6 = models.ImageField(upload_to='media/static/images/tour_images', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Добавления туров"
        verbose_name = "Добавление тура"
        ordering = ['-when_is_tour']


class TourProgram(models.Model):
    how_day = models.IntegerField()
    path_to_tour = models.CharField(max_length=100)
    location_first = models.CharField(max_length=100)
    hours_from_car = models.CharField(max_length=100)
    location_second = models.CharField(max_length=100)
    hours_from_horse = models.CharField(max_length=100)
    location_third = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Программы туров"
        verbose_name = "Программа тура"
        ordering = ['-how_day']


class Price(models.Model):
    price_includes = models.CharField(max_length=100)
    price_includes_2 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_3 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_4 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_5 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_6 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_7 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_8 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_9 = models.CharField(max_length=100, blank=True, null=True)
    price_includes_10 = models.CharField(max_length=100, blank=True, null=True)

    """Что не входит в стоимость"""

    price_not_includes = models.CharField(max_length=100)
    price_not_includes_2 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_3 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_4 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_5 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_6 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_7 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_8 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_9 = models.CharField(max_length=100, blank=True, null=True)
    price_not_includes_10 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.price_includes

    class Meta:
        verbose_name_plural = "Что входит в стоимость и не входит в стоимость"
        verbose_name = "Что входит в стоимость и не входит в стоимость"


class PriceDetails(models.Model):
    person = models.IntegerField(blank=True, null=True, verbose_name="Количество человек: ")
    in_com = models.IntegerField(blank=True, null=True, verbose_name="Общая цена: ")
    per_person = models.IntegerField(blank=True, null=True, verbose_name="Цена за одного человека: ")

    def __str__(self):
        return str(self.per_person)

    class Meta:
        verbose_name = "Цена: "
        verbose_name_plural = "Цены: "



class Tips(models.Model):
    tittle = models.CharField(max_length=100, verbose_name="Заголовок")
    what_to_bring = models.CharField(max_length=100, verbose_name="Список")
    what_to_bring_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_3 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_4 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_5 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_6 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_7 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_8 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_9 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_10 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_11 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_12 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_13 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_14 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    what_to_bring_15 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Список")
    tittle_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Заголовок 2")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name_plural = "Советы"
        verbose_name = "Совет"


class Photo(models.Model):
    image = models.ImageField(upload_to='media/static/images/tour_images/Photo', verbose_name="Добавить фото(обязательно)")
    image_2 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_3 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_4 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_5 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_6 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_7 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_8 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_9 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")
    image_10 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True, verbose_name="Добавить фото(не обязательно)")

    def __str__(self):
        return self.image

    class Meta:
        verbose_name = "Добавить фото"
        verbose_name_plural = "Добавить фото"


class TourDates(models.Model):
    date_from = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата от: ")
    date_up_to = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата до: ")

    def __str__(self) -> str:
        return f"{self.date_from} - {self.date_up_to}"

    class Meta:
        verbose_name = "Добавить дату тура"
        verbose_name_plural = "Добавить дату тура"


class BookingGroupTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Имя: ")
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name="Контакты: ")
    date = models.ForeignKey(TourDates, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Бронирование группового тура"
        verbose_name_plural = "Бронирование групповых туров"


class BookingPrivateTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Имя: ")
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name="Контакты: ")
    date_from = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата от: ")
    date_up_to = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата до: ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бронирование приватного тура"
        verbose_name_plural = "Бронирование приватных туров"


class TourDate(models.Model):
    date_from = models.CharField(max_length=100, blank=False, null=True, verbose_name='Дата от: ')
    date_up_to = models.CharField(max_length=100, blank=False, null=True, verbose_name='Дата до: ')

    def __str__(self):
        return f"{self.date_from} - {self.date_up_to}"

    class Meta:
        verbose_name = "Дата: "
        verbose_name_plural = "Даты: "


