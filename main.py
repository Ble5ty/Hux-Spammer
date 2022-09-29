import discord
from discord.ext import commands
import asyncio
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='^', intents=intents)

with open("settings.json") as file:
    j = json.load(file)
with open("settings.json") as file:
    guildid = int(j["serverid"])
    spammessages = j["spammessages"]
    spamchannel = j["spamchannel"]

#full credits of orginial codes goes to geb, i only did some changes to make it become spammer

async def spam():
    while True:
        guild = bot.get_guild(guildid)
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                if channel.name.__contains__(spamchannel):
                    await channel.send(spammessages)
                    await asyncio.sleep(0.1)
                else:
                    pass

@bot.event
async def on_ready():
    print("The spammer is ready for now!")
    bot.loop.create_task(spam())

bot.run('')