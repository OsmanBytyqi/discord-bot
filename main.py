import discord
import os

from discord import message


client = discord.Client()

 
@client.event
async def on_ready():
    print('Bot is now online and ready for work')




@client.event
async def on_message(message):




    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Welcome to our server')

   
    if message.content == 'stres'or message.content == 'stres shume'or message.content == 'shume stres':
        await message.channel.send('**it\'s gonna be okay**')



@client.event
async def on_message(message):
    if len(message.attachments) > 0: #Checks if there are attachments
       pic_ext = ['.jpg','.png','.jpeg','.gif']
       for file in message.attachments:
            for ext in pic_ext:
                if file.filename.endswith(ext):
                    await message.channel.send('HAHAHAHAHHAHAHAHAHAH ')




      

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')
    



client.run(os.environ['MY_TOKEN'])




