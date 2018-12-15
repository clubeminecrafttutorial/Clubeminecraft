import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def link(ctx):
    await ctx.send("https://clubeminecraft.com.br/")

bot.run('NTIzNDU0ODkwMDE4NzM0MTAy.DvZw8g.iAYuYNTDM2XP2n3S2THt8RV3fUw')
