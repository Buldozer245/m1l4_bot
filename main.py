import discord
from discord.ext import commands
from fonksiyonlar import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def money(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def sifre(ctx, sifre_uzunluğu = 15):
    await ctx.send(gen_pass(sifre_uzunluğu))

@bot.command()
async def sayi(ctx, sayi_uzunluğu = 3):
    await ctx.send(gen_pas(sayi_uzunluğu))

@bot.command()
async def thebestmusic(ctx):
    await ctx.send("https://youtu.be/dQw4w9WgXcQ?t=42")

@bot.command()
async def randomemoji(ctx):
    await ctx.send(emoji_olusturucu())    


bot.run("token yaz")
