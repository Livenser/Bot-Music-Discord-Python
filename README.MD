<div style="font-family: Arial, sans-serif; max-width: 700px; margin: auto; padding: 20px;">
  <h2 style="text-align: center;">🚀 Cara Nyalain Bot Discord Lo</h2>
  <p style="text-align: center;">Gue kasih langkah-langkahnya biar gak bingung. Simpel aja kok, asal ikutin urutannya yaa!</p>

  <ol>
    <li>
      <strong>Install <code>ffmpeg</code></strong><br>
      Pertama-tama, lo harus install ffmpeg dulu. Ini penting banget soalnya bot lo bakal butuh itu buat muter musik.  
      Langsung aja download dari <a href="https://ffmpeg.org/download.html" target="_blank">sini</a>.  
      Abis install, jangan lupa masukin ke PATH biar bisa dipanggil dari mana aja.
    </li>
    <br>
    <li>
      <strong>Bikin API Key YouTube</strong><br>
      Lo buka Google Cloud Console, terus bikin project baru. Habis itu aktifin <em>YouTube Data API v3</em>, dan lo bakal dapet API Key.  
      Simpen baik-baik ya, ini penting buat ambil data dari YouTube ke bot lo.
    </li>
    <br>
    <li>
      <strong>Siapin Token Bot Discord</strong><br>
      Masuk ke <a href="https://discord.com/developers/applications" target="_blank">Discord Developer Portal</a>, terus buat aplikasi baru.  
      Di situ lo tambahin bot dan copy tokennya. Ingat, token ini rahasia, jangan sembarangan share ke orang!
    </li>
    <br>
    <li>
      <strong>Masukin API Key & Token ke File <code>.env</code></strong><br>
      Bikin file baru namanya <code>.env</code>, terus masukin ini ke dalamnya:
      <pre><code>YOUTUBE_API_KEY=isi_api_key_lo_disini
DISCORD_BOT_TOKEN=isi_token_bot_lo_disini</code></pre>
      Pastikan file <code>.env</code> ini ada di direktori yang sama dengan file <code>main.py</code> lo.
    </li>
    <br>
    <li>
      <strong>Jalankan Bot-nya</strong><br>
      Terakhir tinggal buka terminal, masuk ke folder project lo, terus ketik:
      <pre><code>python main.py</code></pre>
      Kalo gak ada error, berarti bot lo udah jalan. Gampang kan?
    </li>
  </ol>

  <p style="text-align: center; font-style: italic;">Udah kelar deh! Kalo ada yang error, tinggal dicek ulang aja.</p>
</div>
