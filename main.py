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
    if message.content=='kur??'or message.content=='kur???' or message.content=='kur????'|message.content=='kur?':
         await message.channel.send('**Very soon**  ')
    
    if message.content == 'cool':
        await message.add_reaction('\U0001F60E')

     


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




