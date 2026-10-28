import os
import discord
from discord.ext import commands, tasks
from datetime import time
from dotenv import load_dotenv
load_dotenv()
token = str(os.getenv('token_discord'))
canal_geral = os.getenv('canal_geral')
intents = discord.Intents.all()
bot = commands.Bot('.', intents = intents)

@bot.event
async def on_ready():
    enviar_mensagem.start()
    print('Bot inicializado com sucesso!')

@bot.event
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    await bot.process_commands(msg)
    # await msg.reply(f'Um usuário {msg.author.mention} enviou uma mensagem no canal {msg.channel.name}!')


@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(canal_geral)
    await canal.send(f'Membro {membro.mention} entrou neste servidor')

@bot.event
async def on_reaction_add(reacao:discord.Reaction, membro:discord.Member):
    await reacao.message.reply(f'O {membro.name} reagiu a menssagem com {reacao.emoji}')

@bot.command()
async def somar(ctx:commands.Context, num1:float, num2:float):
    await ctx.send(f'A soma entre {num1} e {num2} é {num1 + num2}')

@bot.command()
async def enviar_embed(ctx:commands.Context):
    minha_embed = discord.Embed()
    minha_embed.title = 'Titulo da embed'
    minha_embed.description = 'Descrição'

    imagem = discord.File('Avatar Estude a Mudança.jpg','avatar.jpg')
    #imagem_avatar = discord.File(f'{membro.avatar}', 'user_avatar.jpg')

    minha_embed.set_image(url='attachment://avatar.jpg')
    minha_embed.set_thumbnail(url='attachment://avatar.jpg')

    minha_embed.set_footer(text='Esse é o footer da minha embed')

    minha_embed.set_author(name='Wesley', icon_url='https://i.redd.it/dqzgs9lrbx1g1.jpg', url='https://github.com/dablio-dev')

    await ctx.reply(embed = minha_embed, file = imagem)

@tasks.loop(time=time(23, 30))
async def enviar_mensagem():
    canal = bot.get_channel(1564782422850277466)
    await canal.send('Hora de estudar, repetição ativada')

bot.run(token)
