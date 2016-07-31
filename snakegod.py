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
    open('token.txt', 'w')
    sys.exit('Fatal Error: token.txt is not present, made a new empty one.')
if os.stat('token.txt').st_size == 0:
    sys.exit('Fatal Error: token.txt is empty.')
token = open('token.txt')
print('Token Loaded')

print('Loading command prefix...')
if os.path.isfile('prefix.txt') == False:
    open('prefix.txt', 'w')
    sys.exit('Fatal Error: prefix.txt is not present, made a new empty one.')
if os.stat('prefix.txt').st_size == 0:
    sys.exit('Fatal Error: prefix.txt is empty.')
prefix = open('prefix.txt')
pfx = str(prefix.read())
print('Prefix loaded: ' + pfx)

client = discord.Client()

#I love spaghetti!

@client.event
async def on_ready():
    print('Login Details:')
    print('--------------')
    print('Logged in as:')
    print(client.user.name)
    print('--------------')
    print('Bot User ID:')
    print(client.user.id)
    print('--------------')
    print('Finished Loading')

@client.event
async def on_message(message):
    if message.content.startswith(pfx + 'test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith(pfx + 'sleep'):
        print('CMD [sleep] > Sleep invoked...')
        await client.send_message(message.channel, 'Good night...')
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Good morning!')
        print('CMD [sleep] > Slept for 5 seconds.')
    elif message.content.startswith(pfx + 'function'):
        await client.send_message(message.channel, 'Function trigger recognized!')
        print('CMD [function] > Function check triggered.')
    elif message.content.startswith(pfx + 'die'):
        await client.send_message(message.channel, 'Shiro shutting off... Good bye!')
        print('CMD [die] > Shutting off...')
        sys.exit('Closed by command.')
    elif message.content.startswith(pfx + 'echo '):
        print(time.strftime("%c") + "; cmd: echo; " + message.author.name + ": " + message.content[5 + len(pfx):])
        await client.send_message(message.channel, message.content[5 + len(pfx):])
        print('CMD [echo] > Manual echo invoked with messsage: ' + message.content[5 + len(pfx):])
    elif message.content.startswith(pfx + 'hentai'):
        await client.send_message(message.channel, 'For Hentai and other **NSFW** commands go to the #nsfw channel and spam the shit out of them, for more info, type `-commands NSFW` and @Shizuru will tell you what she can provide!')
        print('CMD [hentai] > Pervy perv~')
    elif message.content.startswith(pfx + 'time'):
        await client.send_message(message.channel, current_time)
        print('CMD [time] > Time Written: ' + str(current_time))
    elif message.content.startswith(pfx + 'pcstats'):
        await client.send_message(message.channel, '**MEM Stats:** \n' + str(psutil.virtual_memory()) + '\n\n **CPU Stats:** \n' + str(psutil.cpu_stats()) + '\n\n **CPU Percent:** \n' + str(psutil.cpu_percent(percpu=True)))
        print('CMD [pcstats] > Host PC Stats Checked')
    elif message.content.startswith('<@207266746594361344>'):
        await client.send_message(message.channel, 'Nani desu ka?')
        print('CMD [mentioned] > Metioned by user: ' + str(message.author))
    elif message.content.startswith(pfx + 'invite'):
        await client.send_message(message.channel,'Click this link to invite me to your server: ' +  discord.utils.oauth_url(client_id=207266727132790785, permissions=None, server=None, redirect_uri=None))
        print('CMD [invite] > Invite Link Generated')
    elif message.content.startswith(pfx + 'help'):
        await client.send_message(message.channel, 'I am still very new so the only things I can do are:\n`00test`\n`00sleep`\n`00echo`\n`00time`\n`00pcstats`\n`00invite`\n\n **Have fun~**')
        print('CMD [help] > Help requested by: ' + str(message.author))

client.run(token.read())