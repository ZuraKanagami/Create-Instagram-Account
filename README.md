
---

# Auto Create Account Instagram

Proyek ini adalah skrip otomatis untuk membuat akun Instagram secara otomatis menggunakan Python. Skrip ini memanfaatkan API Instagram dan pustaka Python untuk mengotomatisasi proses pendaftaran akun baru, termasuk mengaktifkan otentikasi dua faktor (2FA) secara otomatis.

## Fitur

- Membuat akun Instagram baru secara otomatis.
- Mengisi data profil seperti nama pengguna, email, dan kata sandi.
- Menyesuaikan pengaturan profil akun setelah dibuat.
- Mengaktifkan otentikasi dua faktor (2FA) secara otomatis untuk keamanan tambahan.

## Prasyarat

Sebelum menjalankan skrip ini, pastikan Anda memiliki hal-hal berikut:

- Python 3.x terinstal di sistem Anda.
- Pustaka Python yang diperlukan (tercantum di bawah).
- Koneksi internet aktif.

## Instalasi

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/ZuraKanagami/Create-Instagram-Account.git
   cd Create-Instagram-Account
   ```

2. **Instal pustaka Python yang diperlukan:**

   ```bash
   pkg update
   pkg upgrade
   pkg install python3
   pkg install git
   pip install bs4
   pip instaall requests
   pip install faker
   
   ```

3. **Konfigurasi**

   Buka file konfigurasi (config.json atau file serupa) dan sesuaikan parameter sesuai kebutuhan Anda, seperti:
   - Nama pengguna (username)
   - Email
   - Kata sandi (password)
   - Aplikasi Autentikasi (untuk 2FA)

   Pastikan Anda telah mengatur semua detail yang diperlukan untuk proses pendaftaran dan 2FA.

## Penggunaan

Jalankan skrip untuk membuat akun Instagram baru dan mengaktifkan 2FA:

```bash
python Run.py
```

Ikuti petunjuk yang muncul di layar untuk menyelesaikan proses pendaftaran dan konfigurasi 2FA. Skrip akan meminta Anda untuk memasukkan kode 2FA yang dikirimkan melalui SMS atau aplikasi autentikator, jika diperlukan.

## Penjelasan 2FA

Otentikasi dua faktor (2FA) adalah metode keamanan tambahan yang memerlukan dua bentuk verifikasi sebelum mengakses akun. Skrip ini secara otomatis mengaktifkan 2FA setelah pembuatan akun untuk meningkatkan keamanan:

- Skrip ini akan mengirimkan permintaan untuk mengaktifkan 2FA melalui antarmuka Instagram.
- Anda akan diminta untuk memasukkan kode yang diterima melalui SMS atau aplikasi autentikator.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan lakukan fork repositori ini dan buat pull request dengan perubahan Anda. Pastikan untuk mengikuti pedoman kontribusi yang ada.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat LICENSE untuk detailnya.

Terima kasih telah menggunakan proyek ini!

---
