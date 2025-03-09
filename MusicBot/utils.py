#;ibray yang digunakan
import aiohttp
import os
from dotenv import load_dotenv

# memat ke .env
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
BASE_URL = 'https://www.googleapis.com/youtube/v3/'

async def search_youtube(query):
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': API_KEY,
        'maxResults': 1
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + 'search', params=params) as response:
            data = await response.json()
            if 'items' in data and len(data['items']) > 0:
                video_id = data['items'][0]['id']['videoId']
                return f"https://www.youtube.com/watch?v={video_id}"
    return None
