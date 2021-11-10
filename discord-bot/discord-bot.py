import discord
import key
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
            
        elif message.content.startswith('pog'):
            await message.channel.send('aw thats POGGERS mum')

        elif message.content.startswith('ngt'):
            await message.channel.send('NYOOOOOOOOOM')

        elif message.content.startswith('welcome to osu'):
            await message.channel.send('click the circles')
        
        elif message.content.startswith('compliment'):
            number1 = random.randint(0,len(firstA)-1)
            number2 = random.randint(0,len(secondA)-1)
            number3 = random.randint(0,len(thirdA)-1)
            text = "You are a "+firstA[number1]+' '+secondA[number2]+' '+thirdA[number3]
            await message.channel.send(text)

# client key
myKey = key.getKey()
client.run(myKey)