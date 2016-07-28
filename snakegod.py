import discord
import asyncio
import sys
import os
import time
import datetime
import psutil

print('Starting up...')
start_time = time.time()
time = time.time()
current_time = datetime.datetime.now().time()
current_time.isoformat()
print('Checking Token...')
if os.path.isfile('token.txt') == False:
    sys.exit('Fatal Error: token.txt is not present')
token = open('token.txt')
if os.stat('token.txt').st_size == 0:
    sys.exit('Fatal Error: token.txt is empty')
print('Token Loaded')

client = discord.Client()

#hello world

print('Connecting to Discord...')

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
        print('CMD [sleep] > Sleep invoked...')
        await client.send_message(message.channel, 'Good night...')
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Good morning!')
        print('CMD [sleep] > Slept for 5 seconds.')
    elif message.content.startswith('00function'):
        await client.send_message(message.channel, 'Function trigger recognized!')
        print('CMD [function] > Function check triggered.')
    elif message.content.startswith('00die'):
        await client.send_message(message.channel, 'Shiro shutting off... Good bye!')
        print('CMD [die] > Shutting off...')
        sys.exit('Closed by command.')
    elif message.content.startswith('00echo '):
        await client.send_message(message.channel, message.content[6:])
        print('CMD [echo] > Manual echo invoked with messsage: ' + message.content[6:])
    elif message.content.startswith('00hentai'):
        await client.send_message(message.channel, 'For Hentai and other **NSFW** commands go to the #nsfw channel and spam the shit out of them, for more info, type `-commands NSFW` and @Shizuru will tell you what she can provide!')
        print('CMD [hentai] > Pervy perv~')
    elif message.content.startswith('00time'):
        await client.send_message(message.channel, current_time)
        print('CMD [time] > Time Written: ' + str(current_time))
    elif message.content.startswith('00pcstats'):
        await client.send_message(message.channel, '**MEM Stats:** \n' + str(psutil.virtual_memory()) + '\n\n **CPU Stats:** \n' + str(psutil.cpu_stats()) + '\n\n **CPU Percent:** \n' + str(psutil.cpu_percent(percpu=True)))
        print('CMD [pcstats] > Host PC Stats Checked')
    elif message.content.startswith('<@207266746594361344>'):
        await client.send_message(message.channel, '... hello')
        print('CMD [mentioned] > Metioned by user:' + message.author)
    elif message.content.startswith('00invite'):
        await client.send_message(message.channel, discord.utils.oauth_url(client_id=207266727132790785, permissions=None, server=None, redirect_uri=None))
client.run(token.read())