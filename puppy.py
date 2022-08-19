import discord
#import keep_alive

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(client.user,' online')

@client.event
async def on_member_join(member):
  print(f'{member} join!')

@client.event
async def on_member_remove(member):
  print(f'{member} leave!')

#keep_alive.keep_alive()
client.run('OTkwODE5OTMyOTU2Njg4NDM0.G0aZl4.5rP_UvjqtEgcQIV5tEeENrDLk26Z1uHlAg1CNs')