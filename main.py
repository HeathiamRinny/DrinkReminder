import asyncio
import discord
from dotenv import load_dotenv
import os
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
USER_ID = os.getenv('USER_ID')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  while True : 
    await asyncio.sleep(3600) #Attendre une heure
    await send_message_to_user()

async def send_message_to_user():
  user = await client.fetch_user(USER_ID)
  await user.send("Hey ! Il est temps de boire de l'eau ! :heart:")                                   #Message envoyé
  await user.send("https://tenor.com/view/mina-aino-agua-minako-aino-drinking-water-gif-23664760")    #Message envoyé numéro 2

client.run(TOKEN)