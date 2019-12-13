import os
import discord
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont
import textwrap
from random import choice

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

client = discord.Client()


def draw_picture(mymsg):
    folder = r"picturefolder/"
    a = choice(os.listdir(folder))
    file = folder +a
    W, H = (300, 200)
    msg = "\n".join(textwrap.wrap(mymsg, width=50))
    background = Image.open(file)
    im = Image.new("RGBA", (W, H), "black")
    draw = ImageDraw.Draw(background)
    w, h = draw.textsize(msg)
    draw.text(((W - w) / 2, (H - h) / 2), msg, fill="white")
    background.save("picturefolder/mypicture.png", "PNG")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return
    if "don't quote me on that" in message.content.lower() and len(message.content.lower()) <= 440:
        draw_picture("\"" + message.content + "\"" + "\n- %s" % message.author)
        with open('picturefolder/mypicture.png', 'rb') as picture:
            await channel.send(file=discord.File(picture))
            os.remove('picturefolder/mypicture.png')


client.run(token)
