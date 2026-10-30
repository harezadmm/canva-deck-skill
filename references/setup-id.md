# Setup skill canva-deck di akun Claude lain

## 1. Pasang skill

- **PC sama, user Windows sama:** skill sudah otomatis ada di semua akun Claude, karena folder `%USERPROFILE%\.claude\skills\canva-deck` dipakai bersama. Lewati langkah ini.
- **PC lain:**
  1. Salin `canva-deck.skill`. File ini adalah zip.
  2. Ekstrak sampai folder `canva-deck` ada di `%USERPROFILE%\.claude\skills\canva-deck\`. Di dalamnya harus langsung ada `SKILL.md`.
  3. Restart Claude Desktop.

## 2. Akun Claude

- Pakai paket berbayar yang punya Claude Code dan Claude in Chrome. **Max disarankan**, karena 4 builder paralel cepat menghabiskan limit.
- Login di Claude Desktop, lalu buka tab **Code**.

## 3. Connector Canva

1. Buka claude.ai, lalu **Settings → Connectors → Canva → Connect**.
2. Login akun Canva Premium.

## 4. Chrome + Claude in Chrome

1. Disarankan profil Chrome terpisah per akun Claude.
2. Pasang ekstensi **Claude in Chrome**, lalu login dengan akun Claude ini.
3. Di Chrome itu, **login Canva Premium sendiri**. Agen tidak boleh login.
4. Bahasa Canva harus **Bahasa Indonesia**, karena aturan memakai nama tombol Indonesia.
5. Izinkan situs `canva.com` di ekstensi.

## 5. Python

1. Pasang Python 3.12+ dari python.org, dan centang "Add to PATH".
2. Lalu jalankan:

```bash
pip install python-pptx lxml pillow
```

## 6. Pakai

Sesi baru di folder mana pun. Ketik `/canva-deck`, atau langsung minta seperti biasa:
1. > Buatkan prompt untuk referensi ini, total 10 prompt ppt: (URL per tema)
2. > /goal kerjakan semua deck pakai multiple subagent, kualitas sama, colorful
3. > sudah jadi semua? kasih semua link

## Catatan

- Satu deck makan waktu sekitar 1,5–2,5 jam. Maksimal sekitar 4 deck jalan bersamaan per komputer.
- Set baru tersimpan di `Downloads\Canva-PPT-Prompts\setN-...`. Skill membaca folder itu untuk menghindari konsep dobel.
- Kalau dua akun dipakai bersamaan, bedakan nomor set-nya.
- Kalau kena limit (HTTP 429), tunggu jam reset, lalu ketik "lanjutkan".
