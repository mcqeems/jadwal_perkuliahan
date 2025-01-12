from django.contrib import admin
from .models import jadwal

admin.site.register(jadwal)
admin.site.site_header = 'Sistem Informasi Jadwal Perkuliahan'
admin.site.site_title = 'Sistem Informasi Jadwal Perkuliahan'
