from discord.ext import commands
import discord
import os
import aiohttp
import lib.dpy_interaction_ui as dpyui

intents = discord.Intents.all()
intents.typing = False
intents.presences = False
intents.members = True

bot = commands.Bot(command_prefix=";", activity=discord.Activity(name="Help --> ;help",
                                                                                             type=discord.ActivityType.playing), status=discord.Status.online, intents=intents, allowed_mentions=discord.AllowedMentions(everyone=False, replied_user=True))

@bot.event
async def on_ready():
    print('Login:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    EXTENSIONS = [filename[:-3]
                for filename in os.listdir("./cog") if filename.endswith(".py")]
    for extension in EXTENSIONS:
        bot.load_extension(f'cog.{extension}')
        print(f"Load:{extension}")

bot.remove_command('help')
bot.load_extension("jishaku")
bot.session = aiohttp.ClientSession(
    headers={
        "User-Agent": "Serves; aiohttp on Python 3.8;"
    },
    skip_auto_headers=["User-Agent"],
    loop=bot.loop
)

bot.ui=dpyui.ui_actions(bot)

with open("token.txt","r") as tokenfile:
    bot.run(tokenfile.readline().strip())