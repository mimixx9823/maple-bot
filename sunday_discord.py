import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Done')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello I am Bot!')
    
bot.run('MTExMDQ4NTUxMjY4ODUwMDc1Nw.GyJCDV.5g6xsGTpXCpYdZdF1VldmCp7625ds4wxyLB2uQ')