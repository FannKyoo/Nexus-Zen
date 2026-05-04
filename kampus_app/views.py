from django.shortcuts import render
from .models import Mahasiswa, Berita, Pesan # Import model Pesan

def beranda(request):
    pesan_sukses = False # Variabel penanda kalau pesan berhasil dikirim

    # LOGIKA MENANGKAP FORM (Jika ada yang klik tombol SEND MESSAGE)
    if request.method == 'POST':
        # Ambil data dari form HTML
        input_nama = request.POST.get('nama')
        input_email = request.POST.get('email')
        input_pesan = request.POST.get('pesan')

        # Simpan ke database
        Pesan.objects.create(
            nama=input_nama,
            email=input_email,
            isi_pesan=input_pesan
        )
        pesan_sukses = True # Ubah status jadi True setelah berhasil simpan

    # Ambil data untuk ditampilkan di halaman (seperti biasa)
    data_berita = Berita.objects.all().order_by('-tanggal')
    data_pengunjung = Mahasiswa.objects.all()

    context = {
        'berita_list': data_berita,
        'pengunjung_list': data_pengunjung,
        'pesan_sukses': pesan_sukses # Kirim status ini ke HTML
    }

    return render(request, 'index.html', context)