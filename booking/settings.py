from django.conf import settings

PAGINATION = getattr(settings, 'DJ_BOOKING_PAGINATION', 10)

BOOKING_SUCCESS_REDIRECT_URL = getattr(settings, 'BOOKING_SUCCESS_REDIRECT_URL', None)

BOOKING_DISABLE_URL = getattr(settings, 'BOOKING_DISABLE_URL', "/")

BOOKING_BG = getattr(settings, 'BOOKING_BG', "img/fam-background.png")

BOOKING_TITLE = getattr(settings, 'BOOKING_TITLE', "Estética FAM")

BOOKING_DESC = getattr(settings, 'BOOKING_DESC', "Agenda sua consulta")

