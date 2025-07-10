import discord
from discord.ext import commands
from typing import List
import random
from modelo import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def suma(ctx, numero1: int, numero2: int):
    await ctx.send(f"la suma de {numero1} con {numero2} es igual a: {numero1 + numero2}")

@bot.command()
async def resta(ctx, numero1: int, numero2: int):
    await ctx.send(f"la suma de {numero1} con {numero2} es igual a: {numero1 - numero2}")

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def datos(ctx):
    datos=[
        "Jupiter es el planeta mas grande del sistema solar",
        "Las jirafas tienen 30 veces más probabilidades de ser alcanzadas por un rayo que las personas. Es cierto que sólo hay cinco rayos mortales bien documentados sobre jirafas entre 1996 y 2010. Pero debido a que la población de la especie es de sólo 140.000 durante este tiempo, esto supone alrededor de 0,003 muertes por rayo por cada mil jirafas cada año. Esto es 30 veces la tasa de mortalidad equivalente para los seres humanos.",
        "el Chimborazo es el volcán mas cercano al sol",
        "Una hamburguesa con queso (o cheeseburger) es una hamburguesa que contiene en su interior unas rodajas de queso procesado (queso americano) ligeramente fundido. En algunas ocasiones se le denomina también como s the most merican' thing ever cr"
    ]
    await ctx.send(random.choice(datos))


@bot.command()
async def ia(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            name = attachment.filename
            url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("¡PERO QUE QUERES QUE HAGA SI NO MANDÁS FOTOO!")

bot.run("")