import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@bot.command(name='')
async def bot_command(ctx):
    
    await ctx.send('')

async def on_message(message):
    if message.author == bot.user:
        return
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("merhaba nasılsın")
    if message.content.startswith('iyiyim sen'):
        await message.channel.send('iyi valla ne olsun')
    elif message.content.startswith('bb'):
        await message.channel.send("git ama geri gel :(")
    
    if message.content.startswith('seni seviyorum'):
        await message.channel.send('╰(*°▽°*)╯bende seni')
    if message.content.startswith('sa'):
        await message.channel.send('as')
    if message.content.startswith('HxH kaç kere bitirdin'):
        await message.channel.send('50yi geçmiştir yav')
    if message.content.startswith('beni seviyormusun'):
        await message.channel.send('Tabiki ❤️')
    if message.content.startswith('babapiromuyum'):
        await message.channel.send('Tabi len')
    if message.content.startswith('!Komut Yardım'):
        await message.channel.send('Komutlar: merhaba,iyiyim sen,bb,seni seviyorum,sa,HxH kaç kere bitirdin,beni seviyormusun,babapiromuyum,yüzde kac babapiroyum,armut severmisin,en ezbobcu kim,bot sahibi,knighterius u tanır mısın,lucuk u tanır mısın,metini tanır mısın,ahmeti tanır mısın,mavtiyi tanır mısın,Robloxmu Minecraft mı,LoLmü Valomu,sevgilin varmı,beyin yakan jjk şeyleri,başka beyin yakan jjk,HxH beyin yakan şeyi,bana eğlenceli birşey yaz,şimdi sen ne işe yarıyon')       
    if message.content.startswith('yüzde kac babapiroyum'):
        await message.channel.send('adamım herkes babapirodur %100 babapirosun sen ❤️')
    if message.content.startswith('armut severmisin'):
        await message.channel.send('oooooo armut mu favorim özellikle yeşil armut' )
    if message.content.startswith('en ezbobcu kim'):
        await message.channel.send('en ezbobcu armut adam,pepsi man,yarım gojo çınardır :D')
    if message.content.startswith('sus'):
        await message.channel.send('sen sus 😑')
    if message.content.startswith('SUS'):
        await message.channel.send('sen sus 😑')
    if message.content.startswith('stfu'):
        await message.channel.send('bro really sad stfu to bot aint no way💀🤫')
    if message.content.startswith('stfu'):
        await message.channel.send('bro really sad stfu to bot aint no way💀🤫')
    if message.content.startswith('ya sus'):
        await message.channel.send('blud criying bc he got roasted by a bot💀💀💀')
    if message.content.startswith('YA SUS'):
        await message.channel.send('blud criying bc he got roasted by a bot💀💀💀')
    if message.content.startswith('bot sahibi'):
        await message.channel.send('@pocky.is.cool arkadaşlık at bence iyi biri :D')
    if message.content.startswith('bot sahibi kim'):
        await message.channel.send('@pocky.is.cool arkadaşlık at bence iyi biri :D')
    if message.content.startswith('sahibin kim'):
        await message.channel.send('@pocky.is.cool arkadaşlık at bence iyi biri :D')
    if message.content.startswith('knighterius u tanır mısın'):
        await message.channel.send('pepsi adam')
    if message.content.startswith('lucuk u tanır mısın'):
        await message.channel.send('tabiki ifşası var bende (lucuk gerçek kürt)')
    if message.content.startswith('metini tanır mısın'):
        await message.channel.send('tabi 6 yaşında değil miydi o ya (metin afgan)(onunda ifşası var :D)')
    if message.content.startswith('ahmeti tanır mısın'):
        await message.channel.send('çocuk menüsü')
    if message.content.startswith('mavtiyi tanırmısın'):
        await message.channel.send('gitsin o ders çalışsın LGSye gircek 💀')
    if message.content.startswith('YA'):
        await message.channel.send('stfu lil nigga 💀')
    if message.content.startswith('YA SEN STFU'):
        await message.channel.send('blud mad😂😂😂')
    if message.content.startswith('Robloxmu Minecraft mı'):
        await message.channel.send('Valo')
    if message.content.startswith('LoLmü Valomu'):
        await message.channel.send('LoL')
    if message.content.startswith('sevgilin varmı'):
        await message.channel.send('yok,ben yanlız bir botum🥹')
    if message.content.startswith('beyin yakan jjk şeyleri'):
        await message.channel.send('sen gojo satoru olduğun içinmi güçlüsün yoksa güçlü olduğun içinmi gojo satarusun...')
    if message.content.startswith('başka beyin yakan jjk'):
        await message.channel.send('yuujinin alan genişletmesi mahitoyu kovaladığı where you go I go what you see I see yeri olabilirmi ne dersin belkile yooriki tenkai dememiş olabilir ama önceden gösterilmiş olabilirmi')
    if message.content.startswith('HxH beyin yakan şeyi'):
        await message.channel.send('Killua başlangıçta avcı sınavında abisini görünce ailesinin yanına dönmüştü.Killua çok güçlü olduğuna göre ordan rahat bir şekilde kaçabilirdi neden kaçmadı ve ona işkence edilmesine izin verdi?')
    if message.content.startswith('bana eğlenceli birşey yaz'):
        await message.channel.send('eğlenceli birşey')
    if message.content.startswith('şimdi sen ne işe yarıyon'):
        await message.channel.send('hiçbi işe yaramıyom 💀')
    if message.content.startswith('yarrak'):
        await message.channel.send('https://tenor.com/tr/view/ohaçet-ne-diyor-gif-19560703')

    


client.run("token here fr")


