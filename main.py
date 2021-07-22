from discord.ext import commands
import discord

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

with open("token.txt","r") as tokenfile:
    bot.run(tokenfile.readline().strip())