from django.contrib import admin

from .models import (
    TourDates,
    TourProgram,
    Tips,
    Price,
    Photo,
    TourAdd,
    BookingGroupTour,
    BookingPrivateTour, PriceDetails
)


class PriceDetailsAdmin(admin.ModelAdmin):
    list_display = 'id person in_com per_person'.split()
    list_display_links = 'id per_person'.split()


admin.site.register(TourAdd)
admin.site.register(TourProgram)
admin.site.register(Price)
admin.site.register(Tips)
admin.site.register(Photo)
admin.site.register(TourDates)
admin.site.register(BookingGroupTour)
admin.site.register(BookingPrivateTour)
admin.site.register(PriceDetails, PriceDetailsAdmin)


