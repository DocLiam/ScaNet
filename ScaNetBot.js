//Bot setup
const Discord = require('discord.js');
const client = new Discord.Client();
const prefix = "!";

var content;
var channel;
var author;
var HelpEmbed;

//Confirmation of connection established
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

//Message received
client.on('message', message => {
  content = message.content
  channel = message.channel
  author = message.author

  if(content.startsWith(prefix)){
    //Help command
    if (content.endsWith("help")) {
      HelpEmbed = new Discord.MessageEmbed()
      .setColor("#a200ff")
      .setTitle("**Help**")
      .setAuthor(author.username, author.avatarURL())
      .addField("!register (User Name) (User Password)", "Register your Discord account as a ScaNet account, with a Username and Password.")
      .addField("!post (GitHub Link) (Code Description)", "Post your code to ScaNet for evaluation or submission using a GitHub URL.");

      channel.send(HelpEmbed);
    }
    //Register command
    if (content.endsWith("register")) {
      channel.send(HelpEmbed);
    }
  }
});

//Bot startup
client.login('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.K7KAlBNFRLwbXPoHL1Hs8t2Q--U');
