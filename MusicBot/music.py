##libray yang digunakan
import discord
import asyncio
import yt_dlp as youtube_dl
from discord.ext import commands
from utils import search_youtube  

# Konfigurasi YouTube-DL
ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

ffmpeg_options = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn -b:a 192k'
}

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=1.0):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []

    def play_next(self, ctx):
        if self.queue:
            next_song = self.queue.pop(0)
            ctx.guild.voice_client.play(next_song, after=lambda e: self.play_next(ctx))

    @commands.hybrid_command(name="play", description="Putar lagu dari YouTube")
    async def play(self, ctx: commands.Context, *, query: str):
        if not ctx.author.voice:
            await ctx.send("Anda harus terhubung ke saluran suara!")
            return
        
        voice_channel = ctx.author.voice.channel
        if ctx.guild.voice_client is None:
            await voice_channel.connect()
        
        if not query.startswith("https://"):
            query = await search_youtube(query)
            if query is None:
                await ctx.send("🚫 Lagu tidak ditemukan.")
                return
        
        async with ctx.typing():
            player = await YTDLSource.from_url(query, loop=self.bot.loop, stream=True)
            if ctx.guild.voice_client.is_playing():
                self.queue.append(player)
                await ctx.send(f"📥 Lagu ditambahkan ke antrean: {player.title}")
            else:
                ctx.guild.voice_client.play(player, after=lambda e: self.play_next(ctx))
                await ctx.send(f"🎵 Sekarang memutar: {player.title}")
    
    @commands.hybrid_command(name="skip", description="Lewati lagu saat ini")
    async def skip(self, ctx: commands.Context):
        if ctx.guild.voice_client and ctx.guild.voice_client.is_playing():
            ctx.guild.voice_client.stop()
            await ctx.send("⏩ Lagu telah dilewati.")
        else:
            await ctx.send("🚫 Tidak ada lagu yang sedang diputar.")
    
    @commands.hybrid_command(name="stop", description="Hentikan lagu saat ini")
    async def stop(self, ctx: commands.Context):
        if ctx.guild.voice_client and ctx.guild.voice_client.is_playing():
            ctx.guild.voice_client.stop()
            self.queue.clear()
            await ctx.send("⏹️ Lagu telah dihentikan dan antrean dikosongkan.")
        else:
            await ctx.send("🚫 Tidak ada lagu yang sedang diputar.")
    
    @commands.hybrid_command(name="leave", description="Putuskan bot dari saluran suara")
    async def leave(self, ctx: commands.Context):
        if ctx.guild.voice_client:
            await ctx.guild.voice_client.disconnect()
            self.queue.clear()
            await ctx.send("👋 Bot telah meninggalkan saluran suara dan antrean dikosongkan.")
        else:
            await ctx.send("🚫 Bot tidak terhubung ke saluran suara.")

async def setup(bot):
    await bot.add_cog(Music(bot))
