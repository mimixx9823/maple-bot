import config.botconfig as config
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, activity=None)
    while True:
        channel = bot.get_channel(config.getChannelId())  # 메시지를 보낼 채널 ID로 바꿔주세요.
        await channel.send('일정 시간마다 실행되는 작업입니다.')
        await asyncio.sleep(5)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello I am Bot!')
    
bot.run(config.getBotToken())