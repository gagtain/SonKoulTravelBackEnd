from django.db import models


class TourAdd(models.Model):
    name = models.CharField(max_length=100)
    tour_time = models.CharField(max_length=100)
    number_of_people = models.IntegerField()
    price = models.IntegerField()
    when_is_tour = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tour_images')
    image_2 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_3 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_4 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_5 = models.ImageField(upload_to='tour_images', blank=True, null=True)
    image_6 = models.ImageField(upload_to='tour_images', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Добавления туров"
        verbose_name = "Добавление тура"
        ordering = ['-when_is_tour']


class TourProgram(models.Model):
    BY_CAR = '1'
    BY_WALK = '2'
    BY_HORSE = '3'
    TRANSPORT_CHOICES = ((BY_CAR, 'Машина'),
                         (BY_HORSE, 'Лошадь'),
                         (BY_WALK, 'Пешком'))
    """Типы локаций"""
    PLACE_SQUAD = '1'
    LUNCH = '2'
    SLEEPING_TIME = '3'
    TYPE_LOCATION_CHOICES = (
        (PLACE_SQUAD, 'Место сбора'),
        (LUNCH, 'Обед'),
        (SLEEPING_TIME, 'Время сна'),
    )
    how_day = models.IntegerField(verbose_name="номер дня")

    location_first = models.CharField(max_length=100, verbose_name="Первая локация")
    type_location_first = models.CharField(max_length=100, choices=TYPE_LOCATION_CHOICES, verbose_name="Тип первой локации")
    first_transport_duration = models.CharField(max_length=100, verbose_name="Длительность первой поездки")
    first_transport_type = models.CharField(max_length=100, choices=TRANSPORT_CHOICES, verbose_name="Тип траспорта")
    location_second = models.CharField(max_length=100, verbose_name="Вторая локация")
    type_location_second = models.CharField(max_length=100, choices=TYPE_LOCATION_CHOICES, verbose_name="Тип второй локации")
    second_transport_duration = models.CharField(max_length=100, verbose_name="Длительность второй поездки")
    second_transport_type = models.CharField(max_length=100, choices=TRANSPORT_CHOICES, verbose_name="Тип транспорта")
    location_third = models.CharField(max_length=100, verbose_name="Третья локация")
    type_location_third = models.CharField(max_length=100, choices=TYPE_LOCATION_CHOICES, verbose_name="Тип третьей локации")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name="Тур", related_name="programs")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Программы туров"
        verbose_name = "Программа тура"
        ordering = ['-how_day']


class Price(models.Model):
    tour = models.OneToOneField(TourAdd, on_delete=models.CASCADE, related_name="prices",
                                verbose_name="Ценовые включения")
    price_includes = models.CharField(max_length=100)
    """Что не входит в стоимость"""
    price_not_includes = models.CharField(max_length=100)

    def __str__(self):
        return self.price_includes

    class Meta:
        verbose_name_plural = "Что входит в стоимость и не входит в стоимость"
        verbose_name = "Что входит в стоимость и не входит в стоимость"


class PriceDetails(models.Model):
    person = models.IntegerField(blank=True, null=True, verbose_name="Количество человек: ")
    in_com = models.IntegerField(blank=True, null=True, verbose_name="Общая цена: ")
    per_person = models.IntegerField(blank=True, null=True, verbose_name="Цена за одного человека: ")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, verbose_name="Тур", related_name="price_details")

    def __str__(self):
        return str(self.per_person)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.in_com = self.per_person * self.person
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = "Цена: "
        verbose_name_plural = "Цены: "


class Tips(models.Model):
    tittle = models.CharField(max_length=100, verbose_name="Заголовок")
    what_to_bring = models.CharField(max_length=100, verbose_name="Список")
    tittle_2 = models.CharField(max_length=100, blank=True, null=True, verbose_name="Заголовок 2")
    description = models.TextField(verbose_name="Описание")
    tour = models.OneToOneField(TourAdd, on_delete=models.Case, related_name="tips", verbose_name="Тур")

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name_plural = "Советы"
        verbose_name = "Совет"


class Photo(models.Model):
    image = models.ImageField(upload_to='media/static/images/tour_images/Photo',
                              verbose_name="Добавить фото(обязательно)")
    image_2 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_3 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_4 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_5 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_6 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_7 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_8 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_9 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                verbose_name="Добавить фото(не обязательно)")
    image_10 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True,
                                 verbose_name="Добавить фото(не обязательно)")
    tour = models.OneToOneField(TourAdd, on_delete=models.CASCADE, verbose_name="Тур", related_name="photos")

    def __str__(self):
        return self.tour.name

    class Meta:
        verbose_name = "Добавить фото"
        verbose_name_plural = "Добавить фото"


class TourDates(models.Model):
    date_from = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата от: ")
    date_up_to = models.CharField(max_length=100, blank=False, null=True, verbose_name="Дата до: ")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="dates", verbose_name="Туры")

    def __str__(self) -> str:
        return f"{self.date_from} - {self.date_up_to}"

    class Meta:
        verbose_name = "Добавить дату тура"
        verbose_name_plural = "Добавить дату тура"


class BookingGroupTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Имя: ")
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name="Контакты: ")
    date = models.ForeignKey(TourDates, on_delete=models.CASCADE, related_name="group_bookings")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="group_bookings")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Бронирование группового тура"
        verbose_name_plural = "Бронирование групповых туров"


class BookingPrivateTour(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True, verbose_name="Имя: ")
    email_or_whatsapp = models.CharField(max_length=100, blank=False, null=True, verbose_name="Контакты: ")
    date = models.DateTimeField(verbose_name="Дата от: ")
    date_up_to = models.DateTimeField(verbose_name="Дата до: ")
    tour = models.ForeignKey(TourAdd, on_delete=models.CASCADE, related_name="private_bookings")

    def __str__(self):
        return self.name + self.email_or_whatsapp + f" - {self.date} - {self.date_up_to}"

    class Meta:
        verbose_name = "Бронирование приватного тура"
        verbose_name_plural = "Бронирование приватных туров"
