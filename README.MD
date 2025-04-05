<!-- Setup Bot Discord - Gaya Santai Anak SMK -->
<section style="font-family: 'Segoe UI', sans-serif; padding: 2rem; max-width: 800px; margin: auto; background: #fefefe; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); color: #2d2d2d;">
  <h2 style="text-align: center; color: #007bff; margin-bottom: 1.2rem;">🛠️ Cara Nyalain Bot Discord Kamu</h2>
  <p style="font-size: 1rem; text-align: center; margin-bottom: 2rem;">
    Nih, gua kasih step-by-step buat nyalain bot Discord lo biar gak ribet. Simple kok, asal ikutin aja urutannya.
  </p>

  <ol style="line-height: 1.9; padding-left: 1rem;">
    <li>
      <strong>Install <code>ffmpeg</code></strong><br>
      Jadi gini, ffmpeg itu penting banget buat jalanin fitur musik di bot lo. Lo tinggal download aja dari 
      <a href="https://ffmpeg.org/download.html" target="_blank" style="color: #007bff;">sini</a>.  
      Kalau udah di-install, jangan lupa masukin ke PATH juga ya, biar bisa dipanggil dari mana aja.
    </li>

    <li>
      <strong>Bikin API Key YouTube</strong><br>
      Masuk ke Google Cloud Console, bikin project baru, terus aktifin "YouTube Data API v3". Abis itu lo bakal dapet API key.  
      Simpen baik-baik ya, jangan asal share. API ini yang ngebantu bot buat ngakses data dari YouTube.
    </li>

    <li>
      <strong>Siapin Token Bot Discord</strong><br>
      Masuk ke <a href="https://discord.com/developers/applications" target="_blank" style="color: #007bff;">Discord Developer Portal</a>, terus bikin aplikasi baru. Tambahin bot ke project-nya, terus lo bakal dapet token.  
      Nah, token ini semacam password buat bot lo, jadi jangan bocorin ke orang lain.
    </li>

    <li>
      <strong>Masukin API Key dan Token ke File <code>.env</code></strong><br>
      Bikin file baru namanya <code>.env</code>, isinya kira-kira gini:
      <pre style="background: #f0f0f0; padding: 1rem; border-radius: 8px;"><code>YOUTUBE_API_KEY=masukin_api_key_lo_disini
DISCORD_BOT_TOKEN=masukin_token_disini</code></pre>
      File ini harus ada di folder utama tempat lo naro <code>main.py</code>. Ini biar bot bisa baca data penting itu.
    </li>

    <li>
      <strong>Jalankan Bot-nya</strong><br>
      Tinggal buka terminal atau CMD, terus ketik:
      <pre style="background: #f0f0f0; padding: 1rem; border-radius: 8px;"><code>python main.py</code></pre>
      Kalau semua udah beres, bot lo langsung nyala. Gampang kan?
    </li>
  </ol>

  <p style="text-align: center; margin-top: 2rem; font-style: italic; color: #555;">
    Udah deh, tinggal dicoba! Kalo ada yang error, cek lagi langkah-langkahnya. Semangat ngoding, bro! 💪✨
  </p>
</section>
