import discord
import random

client = discord.Client()

# compliment stuff

firstA =["lazy", "stupid","insecure", "idiotic", "slimy", "slutty", "smelly", "pompous", "communist", "dicknose", "pie-eating", "racist", "elitist", "white trash", "drug-loving", "butterface", "tone deaf", "ugly", "creepy"]

secondA =["douche", "ass", "turd", "rectum", "butt", "cock", "shit", "crotch", "bitch", "turd", "prick", "slut", "taint", "fuck", "dick", "boner", "shart", "nut", "sphincter"]

thirdA =["pilot", "canoe", "captian", "pirate", "hammer", "knob", "box", "jockey", "nazi", "waffle", "goblin", "blossom", "biscuit", "clown", "socket", "monster", "hound", "dragon", "balloon"]

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
        
        elif message.content.startswith('compliment'):
            number1 = random.randint(0,len(firstA)-1)
            number2 = random.randint(0,len(secondA)-1)
            number3 = random.randint(0,len(thirdA)-1)
            text = "You are a "+firstA[number1]+' '+secondA[number2]+' '+thirdA[number3]
            await message.channel.send(text)

        elif message.content.startswith(''):
            await message.channel.send('oh wow cool')
            await message.channel.send('just dont steal my girl')

# client key
client.run('NzkxNTMxNzUyNjg5NjMxMjgz.X-QhYw.WcMUy1aR-JXjsV9lPYst_hXFTXI')