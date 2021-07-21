#https://realpython.com/how-to-make-a-discord-bot-python/
#https://discord.com/developers/applications/
#https://discordpy.readthedocs.io/en/latest/api.html
# pip install -U discord.py
# pip install -U python-dotenv
# bot.py
import os, discord, random

TOKEN = 'ВАШ-ДИСКОД-ТОКЕН'
DISCORD_GUILD = 'ВАШ#ДИСКОРД-КАНАЛ'

client = discord.Client()

#1
#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

#2
#@client.event
#async def on_ready():
#    for guild in client.guilds:
#        if guild.name == DISCORD_GUILD:
#            break
#
#    print(
#        f'{client.user} is connected to the following guild:\n'
#        f'{guild.name}(id: {guild.id})\n'
#    )
#
#    members = '\n - '.join([member.name for member in guild.members])
 #   print(f'Guild Members:\n - {members}')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

@client.event
async def on_message(message):
    allcommand = f"/? - помощь, /n /x "
    mess_1 = 'YO123'


    if message.author == client.user:
        return
    if message.content == '/?':
        response = (allcommand)
        await message.channel.send(response)

    if message.content == '/1':
        response = (mess_1)
        await message.channel.send(response)



client.run(TOKEN)
