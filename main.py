import discord
import os
from dotenv import load_dotenv
from discord.ext import commands, tasks
load_dotenv()
token = os.getenv('token_discord')
canal_comandos = int(os.getenv('canal_comandos'))
canal_sugestao = int(os.getenv('canal_sugestao'))

intents = discord.Intents.all()
bot = commands.Bot('!sugerir', intents = intents)

@bot.event
async def on_ready():
    print('Bot carregado com sucesso!')

@bot.command()
async def _privado(ctx:commands.Context):
    canal = ctx.channel.id
    if canal != canal_comandos:
        return
    await ctx.author.send(f'Insira o comando !sugerir_particular e logo em seguida a sua sugestão.')

@bot.command()
async def _particular(ctx:commands.Context,* ,sugestao_user):
    if ctx.guild != None:
        return
    sugestao = str(sugestao_user).strip().capitalize()
    await ctx.send(sugestao)

    await disparar_embed(sugestao = sugestao)

async def disparar_embed(sugestao):
    embed_sugestao = discord.Embed()
    embed_sugestao.title = 'Um usuário enviou uma sugestão!'
    embed_sugestao.description = sugestao

    canal_destino = bot.get_channel(int(canal_sugestao))

    await canal_destino.send(embed = embed_sugestao)

@bot.command()
async def _limparc(ctx:commands.Context, quantidade:int = 10):
    if ctx.guild == None:
        return
    await ctx.channel.purge(limit=quantidade + 1)


bot.run(token)