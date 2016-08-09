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
    sys.exit('Fatal Error: config.json is not present.\nIf you didn\'t already, rename config.example.json to config.json and try again.')
else:
    print('config.json present, continuing...')
if os.path.isfile('commands.json') == False:
    sys.exit('Fatal Error: commands.json is not present.\nIf you didn\'t already, rename config.example.json to config.json and try again.')
else:
    print('commands.json present, continuing...')

with open('config.json', 'r', encoding='utf-8') as config_file:
    config = config_file.read()
    config = json.loads(config)
    print('Loaded configuration.')
with open('commands.json', 'r', encoding='utf-8') as commands_file:
    commands = commands_file.read()
    commands = json.loads(commands)
    print('Loaded commands.')

token = (config['Token'])
if token == '':
    sys.exit('Token not provided, please open config.json and place your token.')
pfx = (config['Prefix'])
ownr = (config['OwnerID'])

client = discord.Client()

# Commands
cmd_count = (commands['cmd_count'])
cmd_sleep = (commands['cmd_sleep'])
cmd_test = (commands['cmd_test'])
cmd_die = (commands['cmd_die'])
cmd_echo = (commands['cmd_echo'])
cmd_pcstats = (commands['cmd_pcstats'])
cmd_invite = (commands['cmd_invite'])
cmd_help = (commands['cmd_help'])
cmd_owner = (commands['cmd_owner'])
cmd_report = (commands['cmd_report'])
cmd_setgame = (commands['cmd_setgame'])
cmd_settopic = (commands['cmd_settopic'])
cmd_serverinfo = (commands['cmd_serverinfo'])
cmd_hentai = (commands['cmd_hentai'])

# I love spaghetti!

@client.event
async def on_ready():
    print('\nLogin Details:')
    print('---------------------')
    print('Logged in as:')
    print(client.user.name)
    print('Bot User ID:')
    print(client.user.id)
    print('---------------------\n')
    print('---------------------------------------')
    print('Running discord.py version ' + discord.__version__)
    print('---------------------------------------\n')
    print('STATUS: Finished Loading!')
    print('-------------------------\n')
    print('-----------------------------------------')
    print('Authors: AXAz0r, Awakening, Battlemuffins')
    print('Bot Version: Beta 0.11')
    print('Build Date: 8. August 2016.')
    print('-----------------------------------------\n')

@client.event
async def on_message(message):
    initiator_data = ('by ' + str(message.author) + ' ,UserID: ' + message.author.id + '. Server: ' + message.server.id)
    client.change_status(game=None)
    if message.content.startswith(pfx + cmd_count):
        cmd_name = 'Count'
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp,'<@' + message.author.id + '> You have written {} messages.'.format(counter))
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_sleep):
        cmd_name = 'Sleep'
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        await client.send_message(message.channel, 'Good night...')
        await client.change_status(idle=True)
        await asyncio.sleep(5)
        await client.change_status(idle=False)
        await client.send_message(message.channel, 'Good morning!')
    elif message.content.startswith(pfx + cmd_test):
        cmd_name = 'Test'
        await client.send_message(message.channel, 'Function trigger recognized!')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_die):
        cmd_name = 'Die'
        await client.send_message(message.channel, 'Shiro shutting off... Good bye!')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
        sys.exit('Closed by command.')
    elif message.content.startswith(pfx + cmd_echo + ' '):
        cmd_name = 'Echo'
        await client.send_message(message.channel, message.content[5 + len(pfx):])
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(cmd_hentai):
        await client.send_message(message.channel,
                                  'For Hentai and other **NSFW** commands go to the #nsfw channel and spam the shit out of them, for more info, '
                                  'type `-commands NSFW` and @Shizuru will tell you what she can provide!')
        await client.send_message(message.channel, current_time)
        cmd_name = 'Time'
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_pcstats):
        cmd_name = 'PC Stats'
        await client.send_message(message.channel,
                                  '**MEM Stats:** \n' + str(psutil.virtual_memory()) + '\n\n **CPU Stats:** \n' + str(
                                      psutil.cpu_stats()) + '\n\n **CPU Percent:** \n' + str(
                                      psutil.cpu_percent(percpu=True)))
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith('<@' + client.user.id + '>'):
        cmd_name = 'BOT Mentioned'
        await client.send_message(message.channel, 'Nani desu ka?')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_invite):
        cmd_name = 'Invite'
        await client.send_message(message.channel, 'In progress')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_help):
        cmd_name = 'Help'
        await client.send_message(message.channel, 'Command is a work in progress for dynamic lists, please be patient!\n\nOn the bright side, I\'ll be your doctor!')
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_owner):
        cmd_name = 'Owner Check'
        if message.author.id == ownr:
            await client.send_message(message.channel, '<@' + str(message.author.id) + '> Is the owner')
        else:
            await client.send_message(message.channel, '<@' + str(message.author.id) + '> Is not the owner')
            print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_report + ' '):
        cmd_name = 'Report'
        await client.send_message(message.author, message.content[len(cmd_report) + len(pfx):])
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)
    elif message.content.startswith(pfx + cmd_setgame + ' '):
        cmd_name = 'Set Game'
        GameName = str(message.content[len(cmd_setgame) + len(pfx):])
        game = discord.Game(name=GameName)
        await client.change_status(game)
        print(GameName)
        print('CMD [' + pfx + cmd_name + '] > ' + initiator_data)

client.run(token)