from datetime import datetime
from django.db import models
from django.utils import timezone

class Jurusan(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    nama=models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Jurusan"

class Mahasiswa(models.Model):
    no=models.AutoField(auto_created = True, primary_key=True, serialize=True)
    nama=models.CharField(max_length=100, blank=False, null=False)
    handphone=models.CharField(max_length=12, default="", blank=False, null=False)
    email=models.EmailField(max_length=100, blank=False, null=False)
    nim=models.CharField(max_length=12, blank=False, null=False) 
    id_jurusan=models.ForeignKey(Jurusan, on_delete=models.SET_NULL, null=True)
    timestamp=models.TimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Tabel Mahasiswa"

class Berita(models.Model):
    judul = models.CharField(max_length=200, blank=False, null=False)
    tanggal = models.DateField() # Bisa pilih tanggal saat upload
    isi = models.TextField() # Pakai TextField agar bisa ngetik panjang
    # upload_to='berita/' akan otomatis membuat folder 'berita' di dalam folder media
    gambar = models.ImageField(upload_to='berita/', null=True, blank=True) 

    def __str__(self):
        return self.judul
        
    class Meta:
        verbose_name_plural = "Berita"

class Pesan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    isi_pesan = models.TextField()
    tanggal_kirim = models.DateTimeField(auto_now_add=True) # Otomatis catat waktu pengiriman

    def __str__(self):
        return f"Pesan dari {self.nama}"