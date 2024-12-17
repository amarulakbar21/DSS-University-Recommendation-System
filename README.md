# University Recommendation System

## Data
Data mahasiswa pascasarjana diambil dari [Kaggle University Recommendation Dataset](https://www.kaggle.com/datasets/nitishabharathi/university-recommendation/data).

## Komponen Decision Support System (DSS)

### 1. Database
**Fungsi**: Menyimpan dan mengelola data yang dibutuhkan untuk menghasilkan rekomendasi.

- Menggunakan flat file (CSV) karena data tidak terlalu besar dan tidak memerlukan fitur kompleks.

### 2. Model Analitis
**Fungsi**: Menggunakan algoritma KNN untuk menganalisis data.

**Cara Kerja KNN**:
- Menghitung jarak antara calon mahasiswa dan data mahasiswa sebelumnya berdasarkan fitur nilai GRE, GPA, dan TOEFL.
- Mencari *k* tetangga terdekat (universitas yang relevan).
- Memberikan rekomendasi universitas berdasarkan data universitas tetangga terdekat dengan kemiripan tertinggi.

**Model Prediktif**: Membantu memprediksi kemungkinan kecocokan mahasiswa dengan universitas tertentu.

### 3. Alat Analisis
**Fungsi**: Mendukung pengolahan data, penerapan KNN, dan menghasilkan rekomendasi.

**Alat**:
- **Perangkat Lunak**: Python untuk implementasi KNN. Aplikasi web dibuat menggunakan Python Flask dan framework Bootstrap.
- **Perangkat Keras**: Laptop.

**Manfaat**: Membantu mengakses, mengelola, dan memproses data secara efisien.

### 4. User Interface
**Fungsi**: Memberikan antarmuka yang mudah digunakan bagi calon mahasiswa.

**Contoh**:
- **Antarmuka Berbasis Web**: Calon mahasiswa dapat memasukkan nilai GRE, GPA, dan TOEFL melalui aplikasi web.
- **Visualisasi**: Menampilkan universitas yang direkomendasikan dalam format daftar.

**Manfaat**: Mempermudah pengguna untuk mengakses rekomendasi universitas secara intuitif.

### 5. Kesatuan Pengambilan Keputusan
**Fungsi**: Memanfaatkan hasil DSS untuk membuat keputusan akhir.

**Manfaat**: Membantu memastikan keputusan yang diambil berdasarkan data dan analisis yang relevan.

## Aplikasi Web
Aplikasi Web dibuat menggunakan Python Flask dan framework Bootstrap.

Setelah aplikasi berjalan, halaman beranda akan muncul seperti di bawah ini.

### 1. Tampilan awal:
![Home Page](/images/home1.png?raw=true "Tampilan Awal")

### 2. Tampilan setelah diinputkan nilai:
![Input Page](/images/home2.png?raw=true "Tampilan Input")

### 3. Tampilan hasil sistem rekomendasi:
![Result Page](/images/hasil.png?raw=true "Tampilan Hasil")
