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
    DiscordID = str(ctx.author.id)
    NewUsername = args[0]

    QueryString = "SELECT * FROM BasicUserData\n" + where_table(["DiscordID", "Username"], [('"' + DiscordID + '"'), ('"' + NewUsername + '"')], ["=", "="], ["OR", "OR"], True)
    QueryResult = QueryCursor.execute(QueryString)
    Unauthorised = QueryResult.fetchall()

    if not Unauthorised:
        NewUserID = str(MaxUserID+1)
        NewUserPassword = args[1]
        NewRegisterDate = datetime.now()
        NewCurrencyBalance = str(0)

        QueryString = update_table("BasicUserData", ["UserID", "Username", "UserPassword", "Discord", "DiscordID", "RegisterDate", "CurrencyBalance"], [('"' + NewUserID + '"'), ('"' + NewUsername + '"'), ('"' + NewUserPassword + '"'), ('"' + "Yes" + '"'), ('"' + DiscordID + '"'), ('"' + NewRegisterDate.strftime("%Y-%m-%d %H:%M:%S") + '"'), ('"' + NewCurrencyBalance + '"')], False)
        QueryResult = QueryCursor.execute(QueryString)

        MaxUserID += 1

#Function to set role required for certain tier commands to user specifics
@bot.command()
async def setpermrole(ctx, args*):



@bot.command()
async def manual_query(ctx, userL discord.Member, *args):
    DiscordID = str(ctx.author.id)

    if req_role in user.roles():
        QueryResult = QueryCursor.execute(" ".join(list(args)))

#Bot startup
bot.run('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.K7KAlBNFRLwbXPoHL1Hs8t2Q--U')
