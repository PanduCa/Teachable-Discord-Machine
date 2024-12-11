import discord
from discord.ext import commands
from model import get_class
import os, random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            
            await attachment.save(f"./{file_name}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="./labels.txt", image_path=f"{attachment.filename}"))                                                                             

    else:
        await ctx.send("No se ha subido ninguna imagen")

bot.run("TOKEN")    