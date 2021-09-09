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

    if message.content == 'hello':
        await message.channel.send('Welcome to thenewboston!')

         

    



client.run(os.environ['MY_TOKEN'])




