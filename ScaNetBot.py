#Library imports
import Discord
from discord.ext import commands
import pyodbc
from PythonSQL import *
from datetime import *

#Database setup
DatabaseConn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\progr\Documents\GitHub\ScaNet\ScaNet.accdb;')
QueryCursor = DatabaseConn.cursor()

#Fetching last UserID
QueryString = "SELECT TOP 1 UserID FROM BasicUserData\n" + order_table(["UserID"], ["DESC"], False)
QueryResult = QueryCursor.execute(QueryString)
MaxUserID = QueryResult.fetchall()

#Bot setup
bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    #Confirmation of connection established
    print("Logged in as " + bot.user.name)

#Help command
@bot.command()
async def register(ctx, *args):
    NewUserID = MaxUserID+1
    NewUsername = args[0]
    NewUserPassword = args[1]
    DiscordID = ctx.user.id
    NewRegisterDate = datetime.now()


#Bot startup
bot.run('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.K7KAlBNFRLwbXPoHL1Hs8t2Q--U')
