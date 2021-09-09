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
        await message.channel.send(f'Welcome to our server {message.author}')

    if message.content == 'stres'or message.content == 'stres shume'or message.content == 'shume stres':
        await message.channel.send(f'**it\'s gonna be okay** {message.author}')

    if message.content == 'neser kam provim':
        await message.channel.send(f'**Good luck** {message.author}')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before:` {before.content}\n`'
        f'After: `{after.content}`'
    )        


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')

    



client.run(os.environ['MY_TOKEN'])




