import config.botconfig as config
import webCrowling as web
import discord
import locale
from discord.ext import commands

# Set the locale to Korean
locale.setlocale(locale.LC_TIME, 'ko_KR')

# 반복 작업을 위한 패키지
from discord.ext import tasks
# 현재 시간을 받아와 구조체에 넣어주는 용도로 사용할 패키지
import datetime
# 중복 전송을 방지하기 위해 사용할 패키지
import time

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
check = True

@bot.event
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, activity=None)
        
@tasks.loop(minutes=1)
async def every_hour_notice(self):
    if check :
        now = datetime.datetime.now().weekday()
        if now == 3 or now == 4:    # 목, 금에만
            channel = bot.get_channel(config.getChannelId())  # 메시지를 보낼 채널 ID로 바꿔주세요.
            await channel.send('Check Sunday')
            mapleEvents = web.getMapleEventImgUrlList()
            for url in mapleEvents:
                check = False
                await channel.send(url)

@tasks.loop(hours=24)
async def reset_flag():
    # 현재 요일 확인하기 (0: 월요일, 1: 화요일, ..., 6: 일요일)
    weekday = datetime.datetime.now().weekday()
    if weekday == 0:
        check = True

@bot.command()
async def hello(ctx):
    await ctx.send('Hello I am Bot!')
    
bot.run(config.getBotToken())