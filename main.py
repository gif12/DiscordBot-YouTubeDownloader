from discord.ext import commands
import discord, time, os
from pytube import YouTube
import moviepy.editor as mp
client = commands.Bot(command_prefix='!')
user = discord.Client()
@client.event
async def on_ready():
    print('### F4 TÁ ONLINE ###')

@client.command(name='ajuda')
async def ajuda(ctx):
    await ctx.send('''!mp3 {link} // baixar vídeos .mp3
    !mp4 {link} // baixar vídeos .mp4
    obs: o Discord possui um limite de tamanho de arquivos... se o .mp3/.mp4 não for enviado é porque tem um tamanho superior ao permitido pelo Discord''')

@client.command(name='mp4')
async def mp4(ctx, link):
    print('Baixando...')
    url = link
    title = 'mp4Download'
    video = YouTube(url)
    video = video.streams.get_highest_resolution()
    titname = str(video.title)
    video.download("mp4", filename=f'{title}.mp4')
    print('Download Concluido...')
    try:
        os.rename(rf'mp4/{title}.mp4', rf'mp4/{str(titname)}.mp4')
        await ctx.send(file=discord.File(rf'mp4/{str(titname)}.mp4'))
        os.remove(rf'mp4/{str(titname)}.mp4')
    except:
        await ctx.send(file=discord.File(rf'mp4/mp4Download.mp4'))
        os.remove(rf'mp4/mp4Download.mp4')

@client.command(name='mp3')
async def mp3(ctx, link):
    url = link
    title = 'mp3Download'
    video = YouTube(url).streams.get_audio_only()
    video.download("mp3", filename=f'{title}.mp4')
    titname = str(video.title)
    time.sleep(1)
    clip = mp.AudioFileClip(rf"mp3/{title}.mp4")
    time.sleep(0.5)
    clip.write_audiofile(rf"mp3/{title}.mp3")
    os.remove(rf"mp3/{title}.mp4")
    try:
        os.rename(rf'mp3/{title}.mp3', rf'mp3/{str(titname)}.mp3')
        await ctx.send(file=discord.File(rf'mp3/{str(titname)}.mp3'))
        os.remove(rf'mp3/{str(titname)}.mp3')
    except:
        await ctx.send(file=discord.File(rf'mp3/mp3Download.mp3'))
        os.remove(rf'mp3/mp3Download.mp3')

client.run('DISCORD TOKEN')
