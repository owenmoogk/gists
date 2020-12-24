import discord

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    # checks to make sure it is in the bot channel
    sentChannel = str(message.channel)
    if sentChannel == 'bot':

        # doesnt reply to its own messages
        if message.author == client.user:
            return

        # possibilities
        if message.content.startswith('hello') or message.content.startswith('hi'):
            await message.channel.send('hello!!! ily madiiii')
            await message.channel.send('uwu im simpingg')
            await message.channel.send('u so CUTEEEEE')
            await message.channel.send(':blush::heart:')

        elif message.content.startswith('simp'):
            await message.channel.send('I WILL ONLY SIMP FOR MADI')
            await message.channel.send('SHE IS THE ONLY ONE WORTHY')
            
        elif message.content.startswith('pog'):
            await message.channel.send('aw thats POGGERS mum')

        elif message.content.startswith('ngt'):
            await message.channel.send('NYOOOOOOOOOM')
        
        elif message.content.startswith('madi'):
            await message.channel.send('... is the love of my life')

        elif message.content.startswith('welcome to osu'):
            await message.channel.send('click the circles')

        elif message.content.startswith('who'):
            await message.channel.send('always madi')

        elif message.content.startswith('spam'):
            for i in range(1,30):
                await message.channel.send(":heart:")
            await message.channel.send('im just in love :smiling_face_with_3_hearts:')

        elif message.content.startswith(''):
            await message.channel.send('oh wow cool')
            await message.channel.send('just dont steal my girl')

# client key
client.run('NzkxNTMxNzUyNjg5NjMxMjgz.X-QhYw.fo2y4v_z1mUTTw9tdJxUjuUQhiw')