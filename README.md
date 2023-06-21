## Majelis IT Challenge Chapter #1 Redis from scratch

### 🧾 Pendahuluan
Halo semua, kali ini Majelis IT mengadakan event challenge yang terbuka untuk umum dan khususnya dibuat untuk para member Majelis IT. Sebelumnya Majelis IT telah banyak mengadakan event yang sebagian besar merupakan webinar
sekarang Majelis IT ingin men challenge kalian untuk melakukan software engineering dengan mereplika teknologi yang sudah ada, untuk pada challenge pertama ini kalian di tantang untuk membuat redis dari nol.

<hr>

### 🥇 Benefit mengikuti challenge ini
- Chalege yang tersistemasi dan mudah dalam pengerjaan, pengujian dan penilaianya. selengkapnya tentang teknis akan dijelakan pada point lain di dokumen ini.
- Sarana mempelajari dan memahami teknologi baru dan me reccal dasar dasar computer science.
- Sarana belajar bahasa baru bagi yang ingin menjadikan challenge ini sebagai project dari bahasa yang sedang dipelajari.
- Mengisi waktu luang memacu untuk explorasi lebih dalam bukan hanya mengunakan "redos" tapi paham bagaimana cara kerjanya under the hood
- Tempat Q&A memadai pada group telegram Majelis IT, free dan sangat welcome untuk diskusi dan bertanya satu dengan yang lain di group telegram Majelis IT untuk berbagi dan sharing pengerjaan challenge.
- Prize Saldo Gopay: IDR Rp. 100.000 bagi yang memiliki waktu eksekusi tercepat.

<hr>

### 🔥 Benefit dan learning outcome mengerjakan challenge ini
- Memahami TCP communication
- Memahami tipe data primitif
- Memahami Data struktur Hash Map
- Memahami Optimasi Koneksi TCP
- Memahami menggunakan client redis

<hr>

### 💎 Point Pengujian/Penilaian
- Dapat menerima dan memberi response dari redis protocol: selengkapnya dapat dibaca di https://redis.io/docs/reference/protocol-spec/ sebagai referensi
- Operasi PING dari redis client/library : selengkapnya dapat dibaca di https://redis.io/commands/ping/ sebagai referensi
  - Expected: dikirimkan PING menggunakan redis protocol aplikasi anda harus meresponse dengan PONG [POINT 1]
    ```bash
    (client) -> PING -> (app anda) -> PONG
     ```
- Operasi SET data key value : selengkapnya dapat dibaca di https://redis.io/commands/set/ sebagai referensi
  - Expected: client akan mengirimkan request SET data ke app anda dengan key random uuid dan value angka satu sampai empat dalam string, lalu akan di lakukan operasi GET dari data yang telah di set/kirim [POINT 1]
    ```bash
    (client) -> SET 8313-23-322 satu -> (app anda) -> OK
    (client) -> SET 8313-23-323 dua -> (app anda) -> OK
    (client) -> SET 8313-23-324 tiga -> (app anda) -> OK
    (client) -> SET 8313-23-325 empat -> (app anda) -> OK
    (client) -> SET 8313-23-326 lima -> (app anda) -> OK
    
    (client) -> GET 8313-23-322 -> (app anda) -> satu
    (client) -> GET 8313-23-323 -> (app anda) -> dua
    (client) -> GET 8313-23-324 -> (app anda) -> tiga
    (client) -> GET 8313-23-325 -> (app anda) -> empat
    (client) -> GET 8313-23-326 -> (app anda) -> lima
    ```
- Operasi GET by key : selengkapnya dapat dibaca di https://redis.io/commands/get/ sebagai referensi
  - Expected: client akan mengirimkan request SET data ke app anda dengan key random uuid, lalu diuji jika dilakukan operasi get dengan key yang benar maka akan succes jika salah maka akan None/Null [POINT 1]
    ```bash
    (client) -> SET 8313-23-322 1 -> (app anda) -> OK    
    (client) -> GET 8313-23-322 -> (app anda) -> 1
    (client) -> GET 8313-23-323_# -> (app anda) -> None or negative response redis protocol
    ```
- Operasi DEL untuk menghapus data: selengkapnya dapat dibaca di https://redis.io/commands/del/ sebagai referensi
  - Expected: client akan mengirimkan request SET data ke app anda dengan key random uuid, lalu diuji jika dilakukan operasi delete dengan key yang benar maka jika dilakukan operasi GET maka akan return None/Null [POINT 1]
    ```bash
    (client) -> SET 8313-23-322 1 -> (app anda) -> OK    
    (client) -> DEL 8313-23-322 -> (app anda) -> OK
    (client) -> GET 8313-23-323 -> (app anda) -> None or negative response redis protocol
    ```

- Operasi SET dengan TTL (Time To Live)/kadaluwarsa: selengkapnya dapat dibaca di https://redis.io/commands/set/ sebagai referensi
  - Expected: client akan mengirimkan request SET data ke app anda dengan key random uuid, value dan TTL selama 2 detik, setelah 5 detik akan dilakukan operasi GET maka akan return None/Null [POINT 1]
    ```bash
    (client) -> SET 8313-23-322 1 20 -> (app anda) -> OK  
    -- runtime sleep 5 detik --
    (client) -> GET 8313-23-323 -> (app anda) -> None or negative response redis protocol
    ```


### 📚 Referensi untuk mengerjakan
- https://app.codecrafters.io/courses/redis/overview | !!diharapkan untuk dijadikan referensi bukan copy paste code
- https://www.interviewcake.com/concept/java/hash-map | referensi hashmap

### ⚠️ Peraturan
- Peserta harus mendaftarkan github repo url yang digunakan untuk mengerjakan challenge di https://majelisit-challenge-board.vercel.app/challenge/1
- Peserta dilarang mencurangi sistem penilaian seperti melakukan request untuk menambahkan nilai melalui open endpoint yang kami sediakan, sistem ini bersifat terbuka dan gratis dan untuk bersama kami harapkan tidak melakukan hal yang merusak sistem penilaian
- Tidak ada batas waktu pengerjaan untuk challenge ini bagi yang mau menggunakan sebagai sarana pembelajaran.
- Untuk kateegori eksekusi tercepat batas penilaian adalah pada 1 Agustus 2023.

### 🤩 Tata Cara Mengikuti dan Mengerjakan Challenge

#### Kebutuhan
- Docker pada laptop masing masing. Hasil pengerjaan pada challenge ini harus berjalan di dalam container untuk dapat di uji oleh sistem. Fell free untuk bertanya pada group Majelis IT jika memiliki kendala atau belum pernah menggunakan docker, kami jamin tidak akan sulit.
- Git dan akun Github

#### Pengerjaan
1. Silahkan kunjungi link berikut https://github.com/majelis-it/redis-challenge-template lalu klik `Create a new repository`.

<img width="1236" alt="Screenshot 2023-06-21 at 08 39 45" src="https://github.com/majelis-it/redis-challenge-template/assets/40946917/aeec8714-e5c3-440b-9b69-2f4a2bc7df43">


2. Clone repository baru anda yang telah dibuat dari template yang kami sediakan. lalu kunjungin https://majelisit-challenge-board.vercel.app/challenge/1 untuk mendaftarkan repo anda.

<img width="1431" alt="Screenshot 2023-06-21 at 08 42 01" src="https://github.com/majelis-it/redis-challenge-template/assets/40946917/573d017a-118d-4fde-87cb-f69b98fed3ba">

4. Pada template repo diatas terdapat contoh pengejaan dalam bahasa python namun belum lengkap, anda dapat menggunakan bahasa bebas, tidak ada pembatasan bahasa atau bahkan jika konfigurasi docker container anda melalui pada Dockerfile
5. Kerjakan challenge anda pada folder workspace, pastikan tidak mengubah kode pada folder alatuji.
6. Ubahlah file docker-compose.yml pada bagian `GITHUB_REPO_URL=https://github.com/alfiankan/majelis-it-challenge-board` menjadi link url github repo anda yang di gunakan untuk mengerjakan challenge ini (pastikan sudah terdaftar di https://majelisit-challenge-board.vercel.app/challenge/1)
7. Untuk menguji di local anda dapa menjalankan perintah `docker-compose up --build` pastikan docker sudah menyala dan memiliki koneksi internet
8. Jika sudah yakin dengan hasil pengerjaan silahkan push ke github repo anda
9. Anda dapat melihat hasil pengujian yang anda lakukan di https://majelisit-challenge-board.vercel.app/challenge/1 pada board yang di sediakan klik expand untuk melihat history pengerjaan anda.

<img width="1423" alt="Screenshot 2023-06-21 at 08 42 39" src="https://github.com/majelis-it/redis-challenge-template/assets/40946917/1db8dc28-3e39-4732-848d-1b1f3e757d51">




9. Good Luck
10. Dipersilahkan berdiskusi bebas.




### Join Komunitas Majelis IT untuk saling bertukar ilmu dan bertanya tentang challenge ini
- Join dengan klik link berikut: https://linktr.ee/majelis_it 

