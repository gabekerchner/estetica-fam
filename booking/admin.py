from django.contrib import admin

from booking.models import Booking, BookingSettings


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    site_header = 'Estética FAM'
    list_display = ("nome", "sobrenome", "email", "telefone", "date", "time", "approved")
    list_filter = ("approved", "date")
    ordering = ("date", "time")
    search_fields = ("email", "nome")

admin.site.register(BookingSettings)