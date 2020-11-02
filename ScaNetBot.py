#Library imports
import Discord
from discord.ext import commands
from PythonSQL import *

#Bot setup
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    #Confirmation of connection established
    print("Logged in as " + bot.user.name)

#Help command
@bot.command()



#Bot startup
bot.run('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.K7KAlBNFRLwbXPoHL1Hs8t2Q--U')
