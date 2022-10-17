#Made By shr!ke#0420

#https.//discord.io/evolutes


#Made By shr!ke#0420

#https.//discord.io/evolutes


import discord
import random 


print("""
   _____ _    _ _____  _____ _  ________    ____  _____  
  / ____| |  | |  __ \|_   _| |/ /  ____|  / __ \|  __ \ 
 | (___ | |__| | |__) | | | | ' /| |__    | |  | | |__) |
  \___ \|  __  |  _  /  | | |  < |  __|   | |  | |  ___/ 
  ____) | |  | | | \ \ _| |_| . \| |____  | |__| | |     
 |_____/|_|  |_|_|  \_\_____|_|\_\______|  \____/|_|     
                                                         
                                                         """)

#turn on the intents
client = discord.Client(intents=discord.Intents.all())



bot_token = ''  #bot token
darkwebchannel = 1011316149243359334      #channel id of the darkweb channel
log = 1022530444723503144                 #channel id of the log channel where you want to get the logs
logo = "https://cdn.discordapp.com/attachments/923994945205964851/981405477198004224/420.jpg"   #logo of your rp server (url only)   (optional)
anon_emoji =  '' #darkweb emoji you want to use (':youremoji name: ')       (eg:- ':heart: ' )>> For ❤ This emoji at the Beginning          


@client.event
async def on_ready():
    print('Bot is online!')
    print("Made By shr!ke#0420")
    print(client.user.name)
    activity = discord.Game(name="Watching All The Darkchats !!", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

footermsg = ['wtfshrike <3' , 'Papashrike <3 ','Made By shr!ke#0420']

@client.event
async def on_message(message):
    channel_id = darkwebchannel
    colors = int("0x"+''.join(random.choice('0123456789ABCDEF') for j in range(6)), 16)
    if message.channel.id == channel_id:
        if message.author.bot : return
        author = message.author
        attach = message.attachments
        anon = 'anon'
        if anon in message.content.lower():
            purgeChannel = client.get_channel(darkwebchannel)
            await purgeChannel.purge(limit=1)
            emoji = anon_emoji
            if emoji in message.content:
                await message.channel.send(message.content)
            else:
                await message.channel.send(f"{emoji}" +message.content)
        else:
            await message.channel.purge(limit=1)
            errorformat= discord.Embed(title = 'Please Use The Correct Format !!',description = f'**No More Using Darkweb Emojis <3**',color=(colors))
            errorformat.add_field(name='__Correct Format :__', value='**\n <a:GR_arrows:978234508883144744> Your Darkweb Account Name | Darkweb Message \n \n Example : - Anon111 | Selling Pistols for $69\-**', inline=True)
            errorformat.add_field(name= '__Reply Format : __',value='**\n <a:GR_arrows:978234508883144744> Example:- Anon1111 | Replying to Anon1234 | I AM INTERESTED !! **',inline = False )
            errorformat.set_thumbnail(url=logo)
            errorformat.set_footer(text=(random.choice(footermsg)) , icon_url= 'https://cdn.discordapp.com/attachments/923994945205964851/981405477198004224/420.jpg')
            await author.send(embed=errorformat)
        if len(attach) > 0 :
             for attachment in attach:
                    if attachment.filename.endswith(".jpeg"):
                        await message.channel.send(attach[0].url)
                    if attachment.filename.endswith(".jpg"):
                        await message.channel.send(attach[0].url)
                    if attachment.filename.endswith(".png"):
                        await message.channel.send(attach[0].url)
                    if attachment.filename.endswith(".gif"):
                        await message.channel.send(attach[0].url)
        logchannel = client.get_channel(log)
        logem = discord.Embed(title = f"Message Sent By {message.author}", description =    message.content, color=(colors))
        logem.set_author(name=f"{message.author.name}", icon_url=f"{message.author.avatar}")
        logem.set_footer(text=f"wtfshrike", icon_url= 'https://cdn.discordapp.com/attachments/923994945205964851/981405477198004224/420.jpg')
        await logchannel.send(f"{message.author.mention}" , embed=logem)
                    

client.run(bot_token) 
              

 
