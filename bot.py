import discord
from discord.ext import commands

bot=commands.Bot(commands_prefix='[')

@bot.event
async def on_ready():
print (">>Bot is online<<")

bot.run('NzE3MDMzNTM1MDE3NTgyNzkz.XtYXnw.h4AJGBLA8cjf4JwAG8DS0aeOdos')