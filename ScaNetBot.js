//Bot setup
const Discord = require('discord.js');
const bot = new Discord.Client();
const prefix = "!";

var BotHostGuild;
var BotHostChannel;

var MessageContent;
var MessageChannel;
var MessageAuthor;

var ContentArray;

var HelpEmbed;
var PostEmbed;

var GitHubURL;

//Confirmation of connection established
bot.on('ready', () => {
  BotHostGuild = bot.guilds.cache.get("769355986619596841");
  BotHostChannel = bot.channels.cache.get("769356229310939137");
  BotHostChannel = bot.channels.cache.get("773198263380869139");
  
  console.log(`Logged in as ${bot.user.tag}`);
});

//Message received
bot.on('message', message => {
  MessageContent = message.content;
  MessageChannel = message.channel;
  MessageAuthor = message.author;
  ContentArray = MessageContent.split(" ");

  if(MessageContent.startsWith(prefix)){
    //Help command
    if (ContentArray[0].endsWith("help")) {
      HelpEmbed = new Discord.MessageEmbed()
      .setColor("#a200ff")
      .setTitle("**Help**")
      .setAuthor(MessageAuthor.username, MessageAuthor.avatarURL())
      .addField("!register (User Name) (User Password) (GitHub token)", "Register your Discord account as a ScaNet account, with a Username and Password.", false)
      .addField("!post (GitHub Link)", "Post your repository to ScaNet for evaluation or submission using a GitHub Repository URL. Be sure to have a description in the Repository.", false);

      MessageChannel.send(HelpEmbed);
    }

    //Register command
    if (ContentArray[0].endsWith("register")) {

    }

    //Post command
    if (ContentArray[0].endsWith("post")) {
      GitHubURL = ContentArray[1];

      PostEmbed = new Discord.MessageEmbed()
      .setColor("#7f0000")
      .setTitle("**Newly Posted Repository**")
      .setAuthor(MessageAuthor.username, MessageAuthor.avatarURL())
      .addField("Author ID:", MessageAuthor.id, false)
      .addField("Repository GitHub URL:", GitHubURL, false);

      BotHostChannel.send(PostEmbed);
    }
  }
});

//Bot startup
bot.login('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.K7KAlBNFRLwbXPoHL1Hs8t2Q--U');
