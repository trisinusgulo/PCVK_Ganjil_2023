# -*- coding: utf-8 -*-
"""Week1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nu85Cb8-nDFPgXmzyWAgxOS1aF60M44J
"""

import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow # for image display
from skimage import io
from skimage import transform
from PIL import Image
import matplotlib.pylab as plt

#Membuat lust untuk menyimpan url beberapa image
urls = ["https://iiif.lib.ncsu.edu/iiif/0052574/full/800,/0/default.jpg",
        "https://iiif.lib.ncsu.edu/iiif/0016007/full/800,/0/default.jpg",
        "https://placekitten.com/800/571"]
# baca dan tampilkan image
# loop pada tiap  url image, beberapa image dapat disimpan pada list
for url in urls:
  image = io.imread(url)
  image = cv.resize(image, (0,0), fx=0.5, fy=0.5)
  image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  final_frame = cv.hconcat((image, image_2))
  cv2_imshow(final_frame)
  print('\n')

tinggi = image_2.shape[0]
lebar = image_2.shape[1]
print("resolusi image: tinggi x lebar =" , tinggi," x",lebar)
cv2_imshow(image_2)

image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_3 = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#membuat garis horizontal ditengah image
for y in range (lebar):
  image_3[int((tinggi)/2),y] = [255,255,255]

final_frame = cv.hconcat((image_2, image_3))
cv2_imshow(final_frame)

"""#**Pertanyaan**

1.   Jelaskan, mengapa pada modul praktikum ini eksekusi kode Python dilakukan menggunakan Google Colab?
2.   Jelaskan mengenai kegunaan setiap library pada praktikum langkah ke delapan? Apakah semua library tersebut harus digunakan dalam praktikum sesi ini?
3.   Pada uji coba langkah ke-9 terdapat potongan kode program sebagai berikut :
image = cv.resize(image, (0,0), fx=0.5, fy=0.5)
Apa kegunaan kode program tersebut?dan apa pengaruhnya jika tidak dilakukan?
4.   Perhatikan potongan kode program berikut:
Apakah kegunaan kode [255,255,255] ? Jelaskan!
5.   Jelaskan keterkaitan antara pixel dan juga resolusi gambar yang tinggi ataupun
rendah!

jawaban:

1. Pada modul praktikum, eksekusi kode Python dilakukan melalui Google Colab karena platform ini memberikan kemudahan akses ke sumber daya komputasi cloud seperti GPU dan TPU tanpa perlu konfigurasi rumit. Colab juga memungkinkan kolaborasi dalam pengembangan, penyimpanan di Google Drive, dan penggunaan format notebook interaktif Jupyter untuk menggabungkan kode dan dokumentasi dengan mudah. Ini mempercepat dan menyederhanakan proses belajar serta eksperimen pemrograman Python.
2. Apakah semua library tersebut harus digunakan dalam praktikum sesi ini?**

jawaban:
*  Numpy : Menyediakan Fungsi Bawaan untuk perhitungan Aljabar Linier dan Pembuatan Bilangan Acak
*   Pandas : menyediakan proses analisis data seperti manipulasi data, persiapan data, dan pembersihan data
*   CV2/OpenCV : menyediakan fungsi untuk membaca, membuat, dan menampilkan suatu citra di Python
Scikit-image : pustaka yang digunakan untuk pemrosesan gambar
PIL : untuk memanipulasi file gamba
*   Scikit-image : pustaka yang digunakan untuk pemrosesan gambar
PIL : untuk memanipulasi file gamba
*  Matplotlib : melakukan visualisasi data secara 2D maupun 3D dan menghasilkan suatu gambar yang berkualitas bahkan dapat disimpan dengan format gambar seperti JPEG, JPG, dan PNG. semua library tersebut memiliki keterhubungan satu sama lain sehingg tetap digunakan
3. Potongan kode program image = cv.resize(image, (0,0), fx=0.5, fy=0.5) digunakan untuk mengubah ukuran gambar menjadi setengah dari ukuran aslinya.
*   cv.resize(): Ini adalah fungsi dalam pustaka OpenCV (dalam contoh Anda, ditunjukkan dengan alias cv) yang digunakan untuk mengubah ukuran gambar.
*   image: Ini adalah gambar yang ingin Anda ubah ukurannya.
*   (0,0): Ini adalah titik asal atau titik referensi untuk skala. Dalam hal ini, (0,0) berarti titik asal digunakan sebagai referensi.
*   fx=0.5, fy=0.5: Ini adalah faktor skala yang digunakan untuk merubah ukuran gambar. Dalam kasus ini, fx=0.5 dan fy=0.5 berarti gambar akan diubah ukurannya menjadi setengah dari ukuran aslinya, baik pada sumbu horizontal maupun vertikal.
4. Dalam konteks kode pemrograman yang umumnya berhubungan dengan gambar atau representasi warna, [255, 255, 255] mewakili sebuah nilai warna dalam skala RGB (Red, Green, Blue). Skala RGB digunakan untuk menggambarkan warna dengan mengkombinasikan tiga komponen warna dasar: merah (Red), hijau (Green), dan biru (Blue).
5. Pixel adalah unit terkecil dalam gambar digital yang menyimpan informasi warna. Resolusi gambar mengukur banyaknya piksel dalam gambar per unit panjang atau lebar. Keduanya terkait erat:
*  Resolusi Tinggi: Gambar dengan banyak piksel per unit area memiliki resolusi tinggi. Ini memberikan detail dan ketajaman yang baik pada cetakan berkualitas tinggi dan tampilan berkualitas tinggi di layar.
*  Resolusi Rendah: Gambar dengan sedikit piksel per unit area memiliki resolusi rendah. Detail bisa hilang, dan piksel bisa terlihat jelas, cocok untuk tampilan digital sederhana atau cetakan kecil.

##**Tugas**

1.   Buat garis vertikal dan garis menyilang diagonal pada image keluaran
"""

image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_3 = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#membuat garis verital ditengah image
for x in range(tinggi):
  image_3[x,int((lebar)/2)] = [255,255,255]

final_frame = cv.hconcat((image_2, image_3))
cv2_imshow(final_frame)

image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_3 = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#membaut gari diagonal Menyilang di tengah image
for y in range (lebar):
    image_3[int((tinggi/lebar*y)),y] = [255,255,255]
    image_3[int((tinggi/lebar*y)),(lebar-1-y)] = [255,255,255]

final_frame = cv.hconcat((image_2, image_3))
cv2_imshow(final_frame)

"""2.  Buat garis horisontal berwarna putih dibagian tengah gambar dengan panjang
tertentu
"""

image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_3 = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#Membuat garis horizontal berwarna putih di bagian tengah image
for x in range (tinggi):
  if(x >200 and x < 300):
    image_3[int((tinggi)/2),x] =[255,255,255]

final_frame = cv.hconcat((image_2, image_3))
cv2_imshow(final_frame)

"""3. Buat kotak menggunakan kumpulan pixel warna putih di sembarang tempat dalam
gambar
"""

image_2 = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image_7 = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#membuat kotak menggunakan kumpulan pixel warna putih di sembarang tempat dalam gambar
for y in range (120,200):
  for x in range(120,200):
    image_7[x,y] =[255,255,255]

final_frame = cv.hconcat((image_2, image_7))
cv2_imshow(final_frame)

"""Tugas Kelompok 5"""

urlKTP = cv.imread("/content/KTP.jpeg")
# cv2_imshow(urlKTP)

tinggi = urlKTP.shape[0]
lebar = urlKTP.shape[1]

# kotak putih ditengah
for x in range(280,298):
  for y in range(190,420):
    urlKTP[x,y] = [255, 125, 50]
for v in range(305,325):
  for w in range(190,420):
    urlKTP[v,w] = [0, 0, 255]

# final_frame = cv.hconcat((image_2, image_3))
print("tinggi ", tinggi ," lebar ", lebar)
cv2_imshow(urlKTP)