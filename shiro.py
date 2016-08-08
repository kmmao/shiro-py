import discord
import asyncio
import sys
import os
import time
import datetime
import psutil
import json

print('Starting up...')
start_time = time.time()
time = time.time()
current_time = datetime.datetime.now().time()
current_time.isoformat()

if os.path.isfile('config.json') == False:
    sys.exit(
        'Fatal Error: config.json is not present.\nIf you didn\'t already, rename config.example.json to config.json and try again.')

with open('config.json', 'r', encoding='utf-8') as file:
    config = file.read()
    config = json.loads(config)

token = (config['Token'])
if token == '':
    sys.exit('Token not provided, please open config.json and place your token.')
pfx = (config['Prefix'])
ownr = (config['OwnerID'])

client = discord.Client()

# Commands

report_cmd = 'report '


# I love spaghetti!

@client.event
async def on_ready():
    print('\nLogin Details:')
    print('--------------')
    print('Logged in as:')
    print(client.user.name)
    print('--------------')
    print('Bot User ID:')
    print(client.user.id)
    print('--------------')
    print('Running discord.py version ' + discord.__version__)
    print('--------------')
    print('Finished Loading\n')
    print('Authors: AXAz0r, Awakening, Battlemuffins')
    print('Bot Version: Beta 0.11')
    print('Build Date: 8. August 2016.')


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
        await client.send_message(message.channel, message.content[5 + len(pfx):])
        print('CMD [echo] > Manual echo invoked with messsage: ' + message.content[5 + len(pfx):])
    elif message.content.startswith('hentai'):
        await client.send_message(message.channel,
                                  'For Hentai and other **NSFW** commands go to the #nsfw channel and spam the shit out of them, for more info, type `-commands NSFW` and @Shizuru will tell you what she can provide!')
        print('CMD [hentai] > Pervy perv~')
    elif message.content.startswith(pfx + 'time'):
        await client.send_message(message.channel, current_time)
        print('CMD [time] > Time Written: ' + str(current_time))
    elif message.content.startswith(pfx + 'pcstats'):
        await client.send_message(message.channel,
                                  '**MEM Stats:** \n' + str(psutil.virtual_memory()) + '\n\n **CPU Stats:** \n' + str(
                                      psutil.cpu_stats()) + '\n\n **CPU Percent:** \n' + str(
                                      psutil.cpu_percent(percpu=True)))
        print('CMD [pcstats] > Host PC Stats Checked')
    elif message.content.startswith('<@207266746594361344>'):
        await client.send_message(message.channel, 'Nani desu ka?')
        print('CMD [mentioned] > Metioned by user: ' + str(message.author))
    elif message.content.startswith(pfx + 'invite'):
        await client.send_message(message.channel,
                                  'Click this link to invite me to your server: ' + discord.utils.oauth_url(
                                      client_id=207266727132790785, permissions=None, server=None, redirect_uri=None))
        print('CMD [invite] > Invite Link Generated')
    elif message.content.startswith(pfx + 'help'):
        await client.send_message(message.channel,
                                  'I am still very new so the only things I can do are:\n`' + pfx + 'test`\n`' + pfx + 'sleep`\n`' + pfx + 'echo`\n`' + pfx + 'time`\n`' + pfx + 'pcstats`\n`' + pfx + 'invite`\n\n **Have fun~**')
        print('CMD [help] > Help requested by: ' + str(message.author))
    elif message.content.startswith(pfx + 'owner'):
        if message.author.id == ownr:
            await client.send_message(message.channel, '<@' + str(message.author.id) + '> Is the owner')
        else:
            await client.send_message(message.channel, '<@' + str(message.author.id) + '> Is not the owner')
        print('The owner ID check triggered by ' + str(message.author) + ' ,UserID:' + message.author.id + '. Server: ' + message.server.id)
    elif message.content.startswith(pfx + report_cmd):
        await client.send_message(message.author, message.content[len(report_cmd) + len(pfx):])
        print('Raproted')

client.run(token)
