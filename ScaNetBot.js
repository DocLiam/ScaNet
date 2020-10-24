const Discord = require('discord.js');
const client = new Discord.Client();
const prefix = "!";
var content;

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', message => {
  content = message.content
  channel = message.channel

  if((content.startsWith("!") && channel.type != "dm") || (!content.startsWith("!") && channel.type == "dm")){
    if (content.endsWith("help")) {

    }
    if (content.endsWith("register")) {

    }
  }
});

client.login('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.K7KAlBNFRLwbXPoHL1Hs8t2Q--U');
