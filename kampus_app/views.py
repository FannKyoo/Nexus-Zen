from django.shortcuts import render
from django.core.paginator import Paginator # 1. IMPORT INI DULU
from .models import Mahasiswa, Berita, Pesan

def beranda(request):
    pesan_sukses = False
    
    if request.method == 'POST':
        input_nama = request.POST.get('nama')
        input_email = request.POST.get('email')
        input_pesan = request.POST.get('pesan')
        Pesan.objects.create(nama=input_nama, email=input_email, isi_pesan=input_pesan)
        pesan_sukses = True

    # 2. AMBIL SEMUA BERITA
    semua_berita = Berita.objects.all().order_by('-tanggal')
    
    # 3. ATUR PAGINATION (Misal: 3 Berita per halaman)
    paginator = Paginator(semua_berita, 3) # Angka 3 bisa kamu ganti sesuka hati
    page_number = request.GET.get('page')
    data_berita_paged = paginator.get_page(page_number)

    data_pengunjung = Mahasiswa.objects.all()

    context = {
        'berita_list': data_berita_paged, # 4. Masukkan data yang sudah di-potong-potong ini
        'pengunjung_list': data_pengunjung,
        'pesan_sukses': pesan_sukses
    }

    return render(request, 'index.html', context)