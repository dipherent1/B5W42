"""Telethon-based Telegram scraper (example).
WARNING: You must provide your own API_ID and API_HASH from https://my.telegram.org.
This script fetches recent messages from specified channels and saves to CSV.
"""
import os, csv, asyncio
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()
API_ID = int(os.getenv('TG_API_ID', '0'))
API_HASH = os.getenv('TG_API_HASH', '')
OUTPUT_CSV = os.getenv('OUTPUT_CSV', 'data/telegram_messages.csv')
CHANNELS = os.getenv('CHANNELS', 'channel1,channel2').split(',')  # replace with real channel usernames or ids

async def fetch():
    client = TelegramClient('ethiomart_session', API_ID, API_HASH)
    await client.start()
    rows = []
    async with client:
        for ch in CHANNELS:
            try:
                entity = await client.get_entity(ch)
            except Exception as e:
                print(f"Failed to get entity {ch}: {e}")
                continue
            async for msg in client.iter_messages(entity, limit=500):
                text = msg.message or ''
                media = 'yes' if msg.media else 'no'
                rows.append([msg.id, ch, msg.date.isoformat(), text, media])
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)
    with open(OUTPUT_CSV, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['message_id','channel','timestamp','message','has_media'])
        writer.writerows(rows)
    print(f"Wrote {len(rows)} messages to {OUTPUT_CSV}")

if __name__ == '__main__':
    asyncio.run(fetch())
