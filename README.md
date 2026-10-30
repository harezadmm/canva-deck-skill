# canva-deck

Skill Claude Code untuk membuat presentasi Canva 10 slide yang **colorful, kaya ilustrasi, dan tidak terlalu simpel**. Alurnya dari referensi template Canva sampai link deck jadi.

Skill ini mengatur seluruh proses:
1. menulis prompt deck dari URL template referensi;
2. membuat skeleton `.pptx` dengan python-pptx;
3. membangun deck di Canva lewat Claude in Chrome, satu subagent per deck, berjalan paralel;
4. mengecek hasil dan memberi laporan berisi semua link.

Semua visual diambil dari **Canva Elements** (elemen Pro boleh), dan setiap deck dibuat dari nol. Template referensi hanya dipakai sebagai arah gaya. Isi deck berbahasa Inggris; Claude menjawab dalam bahasa Indonesia singkat.

---

## Hasil

- 10 slide, ukuran 1920 × 1080.
- Satu konsep visual yang unik per deck, dengan sepasang font dari whitelist dan satu transisi.
- Placeholder yang harus diisi sendiri: `[Your Name] · [Organization]` di cover, dan baris kontak di slide 10.
- Deck tersimpan di akun Canva yang login di Chrome. Tidak ada yang di-share, di-download atau di-publish.

---

## Kebutuhan

| Kebutuhan | Keterangan |
|---|---|
| Claude (paket berbayar) | Butuh Claude Code dan Claude in Chrome. **Max disarankan**, karena 4 builder paralel cepat menghabiskan limit. |
| Claude Desktop, tab **Code** | Tempat skill dijalankan |
| Connector **Canva** | Untuk cek progres dan placeholder (`search-designs`, `read-design`) |
| Ekstensi **Claude in Chrome** | Untuk membangun deck di Canva |
| Akun **Canva Premium** | Login sendiri di Chrome, dengan bahasa Canva **Bahasa Indonesia** |
| Python 3.12+ | Dengan `python-pptx`, `lxml` dan `pillow` |

---

## Instalasi

### 1. Pasang skill

Clone repo ini langsung ke folder skills Claude:

```powershell
git clone https://github.com/harezadmm/canva-deck-skill "$env:USERPROFILE\.claude\skills\canva-deck"
```

Pastikan `SKILL.md` ada langsung di dalam `.claude\skills\canva-deck\`, lalu restart Claude Desktop.

> Di PC yang sama dan user Windows yang sama, skill otomatis tersedia untuk semua akun Claude, karena folder `.claude` dipakai bersama.

### 2. Pasang library Python

```bash
pip install python-pptx lxml pillow
```

### 3. Hubungkan Canva

1. Buka claude.ai, lalu **Settings → Connectors → Canva → Connect**, dan login akun Canva Premium.
2. Pasang ekstensi **Claude in Chrome** (disarankan di profil Chrome terpisah per akun Claude), lalu login dengan akun Claude.
3. Di Chrome tersebut, **login Canva sendiri**. Agen tidak pernah login untukmu.
4. Set bahasa Canva ke **Bahasa Indonesia**, karena aturan builder memakai nama tombol Indonesia.
5. Izinkan situs `canva.com` di ekstensi.

Panduan lengkapnya ada di [`references/setup-id.md`](references/setup-id.md).

---

## Cara pakai

Buka sesi baru di tab Code (folder bebas). Ketik `/canva-deck`, atau langsung minta seperti biasa; skill terpanggil otomatis.

### Langkah 1: buat prompt

```
Buatkan prompt untuk referensi ini, total 10 prompt ppt:
New Year:
https://www.canva.com/templates/...
https://www.canva.com/templates/...
Business Plan:
https://www.canva.com/templates/...
```

Hasilnya:
- Claude membuat folder set baru di `Downloads\Canva-PPT-Prompts\setN-<tema>\`.
- Satu subagent penulis per tema berjalan paralel.
- Claude mengecek seluruh set supaya tidak ada konsep, pasangan font atau transisi yang dobel, termasuk terhadap set-set lama di `references/history/`.

### Langkah 2: bangun semua deck

```
/goal kerjakan semua deck pakai multiple subagent, kualitas sama, colorful
```

Claude akan:
1. membuat 10 skeleton `.pptx` secara paralel lalu memvalidasinya;
2. menjalankan **1 builder per deck**, maksimal **4 bersamaan**; begitu satu selesai, deck berikutnya dimulai;
3. mengecek tiap deck dengan `read-design`. Selama masih ada teks `HERO:`, `ICON:` atau `DECOR:`, deck dianggap belum selesai.

### Langkah 3: cek hasil

```
sudah jadi semua? kasih semua link
```

Laporan akhir berisi:
- link edit tiap deck beserta transisinya;
- kekurangan jujur per deck;
- placeholder yang perlu diisi;
- desain sisa yang perlu dihapus manual.

---

## Struktur repo

```
canva-deck/
├── SKILL.md                     # Instruksi utama skill (alur 3 fase + aturan)
├── README.md                    # File ini
├── references/
│   ├── pipeline.md              # Rulebook: §A aturan keras, §B checklist kekayaan visual, §C pipeline, §D pelajaran + whitelist font
│   ├── prompt-writer-brief.md   # Brief untuk subagent penulis prompt
│   ├── skeleton-brief.md        # Brief untuk subagent pembuat skeleton
│   ├── builder-brief.md         # Brief untuk subagent builder di Canva
│   ├── setup-id.md              # Panduan setup (Bahasa Indonesia)
│   ├── examples/                # 3 prompt jadi sebagai standar kualitas
│   └── history/                 # Semua prompt lama (set 5–9), agar konsep tidak terulang
└── scripts/
    ├── table-tournament.py      # Contoh generator skeleton (gaya fun/game)
    └── idea-to-plan.py          # Contoh generator skeleton (gaya bisnis)
```

---

## Aturan penting

Aturan ini dijaga oleh skill, karena melindungi akun Canva dan pekerjaan klien:

- **Dibuat dari nol.** Semua visual dari Canva Elements. Jangan pernah "Gunakan template ini" dan jangan menyalin layout referensi.
- **Tanpa Canva AI:** tidak memakai Magic Media, Dream Lab, Magic Design/Write atau Tanya Canva.
- **Tidak ada aksi keluar:** tidak Bagikan, Unduh atau Publish, tidak mengubah akses, tidak login, dan tidak menghapus desain.
- **Jangan klik "Ubah semua"**, dan tidak copy/paste, karena semua agen berbagi satu clipboard.
- **Font hanya dari whitelist:** Alfa Slab One, Shrikhand, Lilita One, Press Start 2P, Poppins, Nunito, Rubik, Chewy, Quicksand, Luckiest Guy, Archivo Black, DM Sans, Fredoka. Boogaloo, Pixelify Sans, Outfit dan Lexend jatuh ke font lain saat import.
- Tidak ada logo, merek, karakter bermerek atau orang sungguhan.

---

## Tips dan troubleshooting

| Situasi | Solusi |
|---|---|
| Kena limit (HTTP 429) | Tunggu jam reset, lalu ketik `lanjutkan`. Builder dilanjutkan, bukan dibuat ulang, supaya tidak ada desain dobel. |
| Chrome lambat | Maksimal sekitar 4 deck paralel per komputer. Editor Canva hanya merender tab yang aktif. |
| Skill tidak muncul | Cek `SKILL.md` ada langsung di `.claude\skills\canva-deck\`, lalu restart Claude Desktop. |
| Error path terlalu panjang | Windows membatasi path di bawah 260 karakter. Pakai folder pendek (Downloads aman). |
| Script skeleton gagal | Jalankan dengan `python file.py` biasa, bukan `python -I`. |
| Dua akun jalan bersamaan | Bedakan nomor set, dan pakai profil Chrome berbeda per akun. |

Satu deck butuh sekitar **1,5–2,5 jam**. Target realistis: 10 deck per hari tanpa mengurangi kekayaan visual.

---

## Update skill

Setelah skill diubah di satu PC:

```powershell
cd "$env:USERPROFILE\.claude\skills\canva-deck"
git add -A
git commit -m "Update rules"
git push
```

Di PC lain:

```powershell
cd "$env:USERPROFILE\.claude\skills\canva-deck"
git pull
```

Setiap set baru sebaiknya disalin ke `references/history/` lalu di-push, supaya semua akun tahu konsep yang sudah dipakai.
