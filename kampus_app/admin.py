from django.contrib import admin

from import_export import resources, fields
from import_export.admin import ImportExportMixin

from .models import Berita, Mahasiswa, Jurusan, Pesan

admin.site.register(Jurusan)
admin.site.register(Mahasiswa)
admin.site.register(Berita)
admin.site.register(Pesan)