//Bot setup
const Discord = require('discord.js');
const client = new Discord.Client();
const prefix = "!";

var content;
const helpEmbed = new Discord.MessageEmbed()
  .setColor("#ff2f00")
  .setTitle("**Help**");

//Confirmation of connection established
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

//Message received
client.on('message', message => {
  content = message.content
  channel = message.channel

  if(content.startsWith("!")){
    //Help command
    if (content.endsWith("help")) {
      channel.send(helpEmbed);
    }
    //Register command
    if (content.endsWith("register")) {
      channel.send(helpEmbed);
    }
  }
});

//Bot startup
client.login('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.K7KAlBNFRLwbXPoHL1Hs8t2Q--U');
