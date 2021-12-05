import discord
import os

from discord import message


client = discord.Client()

 
@client.event
async def on_ready():
    print('Bot is now online and ready for work')




@client.event
async def on_message(message):

    extension = ['.jpg','.png','.jpeg']



    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Welcome to our server')

    for ext in extension:
        if message.content.endswith(ext):
            await message.channel.send("hello there")

    if message.content == 'stres'or message.content == 'stres shume'or message.content == 'shume stres':
        await message.channel.send('**it\'s gonna be okay**')








          


@client.event
async def on_message_edit(before, after):
    if message.author=='1026#9294':
        return
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before:` {before.content}\n`'
        f'After: `{after.content}`'
    )        


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

    



client.run(os.environ['MY_TOKEN'])




