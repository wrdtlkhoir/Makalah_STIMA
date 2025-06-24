# Pencarian ATM Terdekat di ITB Ganesha dengan Algoritma Uniform Cost Search (UCS)

## 📋 Informasi Proyek
**Nama:** Wardatul Khoiroh  
**NIM:** 13523001  
**Mata Kuliah:** Strategi Algoritma (STIMA)  
**Semester:** 4  

## 📖 Deskripsi
Aplikasi GUI berbasis Python yang menggunakan algoritma **Uniform Cost Search (UCS)** untuk mencari jalur terpendek menuju ATM terdekat di kawasan ITB Ganesha. Aplikasi ini membantu mahasiswa dan pengunjung ITB menemukan ATM dengan rute optimal berdasarkan lokasi mereka saat ini.

## ✨ Fitur
- 🗺️ **Visualisasi Peta ITB** - Menampilkan peta kampus ITB Ganesha
- 🏧 **Pencarian Multi-Bank** - Mendukung ATM dari 6 bank: BNI, BRI, Mandiri, BCA, Bukopin, dan Niaga
- 🔍 **Algoritma UCS** - Implementasi algoritma Uniform Cost Search untuk pencarian jalur optimal
- 📍 **41 Lokasi Campus** - Mencakup semua gedung dan fasilitas utama di ITB
- 🧭 **Petunjuk Arah** - Memberikan langkah-langkah detail untuk mencapai ATM
- 💳 **Info ATM Bersama** - Semua ATM mendukung jaringan ATM Bersama

## 🛠️ Teknologi yang Digunakan
- **Python 3.x**
- **Tkinter** - GUI framework
- **PIL (Pillow)** - Image processing
- **Heapq** - Priority queue untuk implementasi UCS

## 📁 Struktur File
```
Makalah_STIMA/
├── pencarian_atm_itb.py    # File utama aplikasi
├── peta_itb.png           # Peta kampus ITB Ganesha
└── README.md              # Dokumentasi proyek
```

## 🚀 Cara Menjalankan
1. **Install Dependencies:**
   ```bash
   pip install pillow
   ```

2. **Pastikan file peta tersedia:**
   - File `peta_itb.png` harus berada di direktori yang sama dengan `pencarian_atm_itb.py`

3. **Jalankan aplikasi:**
   ```bash
   python pencarian_atm_itb.py
   ```

## 🎯 Cara Penggunaan
1. **Masukkan Lokasi Asal** - Ketik nama lokasi di ITB (contoh: "Labtek V - PIKSI, Teknik Informatika")
2. **Pilih Bank (Opsional)** - Masukkan kode bank (BNI, BRI, MANDIRI, BCA, BUKOPIN, NIAGA) atau kosongkan untuk semua ATM
3. **Klik "Cari ATM Terdekat"** - Sistem akan menampilkan:
   - Jalur optimal menuju ATM
   - Total jarak tempuh
   - Langkah-langkah detail perjalanan

**Karakteristik UCS:**
- Menggunakan priority queue untuk eksplorasi node
- Menjamin solusi optimal (jalur terpendek)
- Biaya uniform 10 meter per edge
- Kompleksitas waktu: O(b^(C*/ε)) dimana C* adalah biaya solusi optimal

## 🎓 Pembelajaran

## 📝 Catatan
- Jarak dihitung dalam satuan meter dengan asumsi 10 meter per koneksi
- Graf dibuat bidirectional untuk memungkinkan perjalanan dua arah
- Semua ATM mendukung jaringan ATM Bersama untuk kemudahan akses

---
*Dibuat sebagai tugas Makalah Strategi Algoritma - Semester 4*
