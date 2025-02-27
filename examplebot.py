import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)

client.run('NzE4NzUxOTY1Mzc0NDQ3NjI2.XttdQg.MRiN3IxdUx-lxwA9sW1OixFSN0Y')