import discord
import asyncio
import sys
import os
import time
import datetime
import psutil

start_time = time.time()
time = time.time()
current_time = datetime.datetime.now().time()
current_time.isoformat()

token = open('token.txt')

client = discord.Client()

#hello world

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print('Bot User ID:')
    print(client.user.id)
    print('Finished Loading')

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
        await client.send_message(message.channel, 'Good night...')
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Good morning!')
    elif message.content.startswith('00function'):
        await client.send_message(message.channel, 'Function trigger recognized!')
    elif message.content.startswith('00die'):
        await client.send_message(message.channel, 'Shiro shutting off... Good bye!')
        sys.exit('Closed by command.')
    elif message.content.startswith('00restart'):
        await client.send_message(message.channel, 'Shiro restarting...')
        os.execv('snakegod.py')
        sys.exit('Restarting.')
    elif message.content.startswith('00echo '):
        await client.send_message(message.channel, message.content[6:])
    elif message.content.startswith('00hentai'):
        await client.send_message(message.channel, 'For Hentai and other **NSFW** commands go to the #nsfw channel and spam the shit out of them, for more info, type `-commands NSFW` and @Shizuru will tell you what she can provide!')
    elif message.content.startswith('00time'):
        await client.send_message(message.channel, current_time)
    elif message.content.startswith('00pcstats'):
        await client.send_message(message.channel, 'Memory Data:')
        await client.send_message(message.channel, psutil.virtual_memory())
        await client.send_message(message.channel, 'CPU Data:')
        await client.send_message(message.channel, psutil.cpu_stats())
client.run(token.read())