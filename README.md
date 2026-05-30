# File-Sharing-Man-upgradeAddbutton

Bot Telegram untuk menyimpan Posting atau File yang dapat Diakses melalui Link Khusus.
Saya Kira Ini Akan Bermanfaat Bagi Banyak Orang.

## ⚠️ Disclaimer

```
Saya tidak bertanggung jawab atas penyalahgunaan bot ini.
Bot ini dimaksudkan untuk membantu untuk menyimpan file yang diinginkan yang dapat diakses melalui Link Khusus.
Gunakan bot ini dengan risiko Anda sendiri, dan gunakan bot ini dengan bijak.
```

### Features
- Sepenuhnya dapat dicustom.
- Dapat di-deploy di heroku & vps.
- Pesan sambutan & Forcesub yang dapat dicustom.
- Lebih dari satu Posting dalam Satu Link (batch).
- Fleksibel FSUB Button bisa 1 button atau 2 button menyesuaikan dengan var yang di isi.

### Setup

- Tambahkan bot ke Channel Database dengan semua izin admin
- Tambahkan bot ke Channel ForceSub tambahkan bot sebagai ADMIN
- Tambahkan bot ke Group ForceSub tambahkan bot sebagai ADMIN
- ENV WAJIB
TG_BOT_TOKEN
OWNER 
OWNER_ID
APP_ID
API_HASH
CHANNEL_ID
MONGO_URI




## 🛡 Installation
### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://risman.vercel.app/file-deploy.html)</br>

**Tonton Video Tutorial Ini di YouTube untuk Bantuan memasang di Heroku**<br>
<a href="https://youtu.be/O2tieQgzYZg">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

<details>
<summary><h3><b>🔗 Extra Custom & List Vars</b></h3></summary>

### ### Variables

* `TG_BOT_TOKEN` Dapatkan Token Bot dari @BotFather

* `APP_ID` Dapatkan API ID dari my.telegram.org

* `API_HASH` Dapatkan API HASH dari my.telegram.org

* `OWNER` Username Telegram Owner Bot (tanpa @)

* `OWNER_ID` User ID Telegram Owner (Super Admin)

* `CHANNEL_ID` ID Channel Database tempat menyimpan file. Contoh: `-100xxxxxxxxxx`

* `MONGO_URI` URI Database MongoDB untuk menyimpan data bot dan admin.

* `ADMINS` User ID Admin Bot. Gunakan spasi untuk memisahkan beberapa ID.

* `PROTECT_CONTENT`

  * `True` = File tidak bisa di-forward dan disimpan.
  * `False` = File bisa di-forward dan disimpan.

* `START_MESSAGE` (Opsional)
  Pesan yang ditampilkan saat pengguna menjalankan perintah `/start`.
  Mendukung format HTML.

* `FORCE_SUB_MESSAGE` (Opsional)
  Pesan yang ditampilkan saat pengguna belum memenuhi syarat akses.
  Mendukung format HTML.


### Extra Variables

* `CUSTOM_CAPTION` letakkan teks teks Kustom Anda jika Anda ingin Mengatur Teks Kustom, Anda dapat menggunakan HTML dan <a href='https://github.com/mrismanaziz/File-Sharing-Man/blob/main/README.md#custom_caption'>fillings</a> untuk pemformatan (hanya untuk dokumen)
* `DISABLE_CHANNEL_BUTTON` Masukan True untuk Nonaktifkan Tombol Berbagi Saluran, Default jika False

### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption

</details>

## 🏷 Support   
- Follow Channel [@Lunatic0de](https://t.me/Lunatic0de) untuk info Update bot 
- Gabung Group [@SharingUserbot](https://t.me/SharingUserbot) untuk diskusi, pelaporan bug, dan bantuan tentang File-Sharing-Man.

## 👨🏻‍💻 Credits

-  [Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)
-  [Risman](https://github.com/mrismanaziz) for [File-Sharing-Man](https://github.com/mrismanaziz/File-Sharing-Man)
-  Based on [CodeXBotz](https://github.com/CodeXBotz) Repo [File-Sharing-Bot](https://github.com/CodeXBotz/File-Sharing-Bot)

## 📑 License
[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)  

[FILE-SHARING-BOT](https://github.com/mrismanaziz/File-Sharing-Man/) is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the
[GNU General Public License](https://www.gnu.org/licenses/gpl.html) as
published by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version. 

##

   **Berikan Bintang Repo ini jika Anda menyukainya ⭐⭐⭐⭐⭐**

