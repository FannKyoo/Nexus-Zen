from django.contrib import admin

from import_export import resources, fields
from import_export.admin import ImportExportMixin

from .models import Berita, Pengunjung, Jurusan, Pesan

admin.site.register(Jurusan)


class BeritaAdmin(admin.ModelAdmin):
    # Tampilkan sebagai kolom (Pastikan 'nama' dan 'email' sesuai dengan yang ada di models.py)
    # Kalau di models.py nama field isinya 'isi_pesan' atau 'pesan', tinggal tambahin di sebelah 'email'
    list_display = ('judul', 'tanggal') 
    
    # Tambahkan fitur Search Bar di atas tabel
    search_fields = ('judul', 'tanggal')
    
    # Batasi jumlah data yang tampil per halaman (Pagination)
    list_per_page = 10

# Daftarkan model Berita dengan pengaturan BeritaAdmin yang baru kita buat
admin.site.register(Berita, BeritaAdmin)

class PengunjungAdmin(ImportExportMixin, admin.ModelAdmin):
    # Tampilkan sebagai kolom (Pastikan 'nama' dan 'email' sesuai dengan yang ada di models.py)
    # Kalau di models.py nama field isinya 'isi_pesan' atau 'pesan', tinggal tambahin di sebelah 'email'
    list_display = ('nama', 'id', 'email', 'jurusan', 'handphone') 
    
    # Tambahkan fitur Search Bar di atas tabel
    search_fields = ('nama', 'email', 'id', 'jurusan','handphone')
    
    list_filter = ('jurusan',)
    
    # Batasi jumlah data yang tampil per halaman (Pagination)
    list_per_page = 10

# Daftarkan model Pengunjung dengan pengaturan PengunjungAdmin yang baru kita buat
admin.site.register(Pengunjung, PengunjungAdmin)

class PesanAdmin(admin.ModelAdmin):
    # Tampilkan sebagai kolom (Pastikan 'nama' dan 'email' sesuai dengan yang ada di models.py)
    # Kalau di models.py nama field isinya 'isi_pesan' atau 'pesan', tinggal tambahin di sebelah 'email'
    list_display = ('nama', 'email', 'isi_pesan') 
    
    # Tambahkan fitur Search Bar di atas tabel
    search_fields = ('nama', 'email')

    # Batasi jumlah data yang tampil per halaman (Pagination)
    list_per_page = 10

# Daftarkan model Pesan dengan pengaturan PesanAdmin yang baru kita buat
admin.site.register(Pesan, PesanAdmin)