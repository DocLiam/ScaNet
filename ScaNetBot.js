const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});

client.login('NzY5MzQ0NTE1NDA3NzQwOTU5.X5Np6g.8YSR_H751Nk_wDrsVIchdwt4Ka8');
