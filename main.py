import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Bot is now online and ready for work')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'stres shume':
        
        await message.channel.send('`it\'s gonna be okay! :)` ')

    if message.content=='depresion':
         await message.channel.send('`it\'s gonna be okay! :)` ')

    if message.content=='neser kam provim':
         await message.channel.send('`Good luck !!! :)` ')




client.run(os.environ['MY_TOKEN'])




