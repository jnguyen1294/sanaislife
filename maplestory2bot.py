import discord
import os

def requestToken():
    tokenAdd = str(os.environ.get(token))
    return tokenAdd

client = discord.Client()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
client.run(requestToken())
#NDQzNTY5NzU3ODA3OTY4MjU2.DdPycQ.wzKxgVcytX3sbvslj5zZg32sLmU
