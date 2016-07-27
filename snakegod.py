import discord
import asyncio
import sys
import os
import time

start_time = time.time()
time = time.time()

token = open('token.txt')

client = discord.Client()

#hello world

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('00test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('00sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('00function'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Function trigger recognized!')

    elif message.content.startswith('00die'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Shiro shutting off... Good bye!')
        sys.exit('Closed by command.')

    elif message.content.startswith('00restart'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Shiro restarting...')
        os.execv('snakegod.py')
        sys.exit('Restarting.')

    elif message.content.startswith('00echo '):
        print(time.strftime("%c") + "; cmd: echo; " + message.author.name + ": " + message.content[6:])
        await client.send_message(message.channel, message.content[6:])


    elif message.content.startswith('00hentai'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'For Hentai and other **NSFW** commands go to the #nsfw channel and spam the shit out of them, for more info, type `-commands NSFW` and @Shizuru will tell you what she can provide!')


client.run(token.read())