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


class Tips(models.Model):
    tittle = models.CharField(max_length=100)
    what_to_bring = models.CharField(max_length=100)
    what_to_bring_2 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_3 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_4 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_5 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_6 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_7 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_8 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_9 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_10 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_11 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_12 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_13 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_14 = models.CharField(max_length=100, blank=True, null=True)
    what_to_bring_15 = models.CharField(max_length=100, blank=True, null=True)
    tittle_2 = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class Photo(models.Model):
    image = models.ImageField(upload_to='media/static/images/tour_images/Photo')
    image_2 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_3 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_4 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_5 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_6 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_7 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_8 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_9 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)
    image_10 = models.ImageField(upload_to='media/static/images/tour_images/Photo', blank=True, null=True)


    def __str__(self):
        return self.image
