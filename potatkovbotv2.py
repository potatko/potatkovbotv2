import math
import discord
import random
import shutil
import asyncio
import os
import youtube_dl
from discord.ext import commands





client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(".help <3"))
    print("Ideme na to :)")

@client.event
async def on_member_join(member):
    
    print(f"{member} zavítal na Kamarátsky spolok vitaj degeš")



@client.event
async def on_member_remove(member):
    print(f"{member} vypadol het F in a chat")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Neexistuje!")

@client.command()
async def filip(ctx):
    filipfotky = ["https://cdn.discordapp.com/attachments/315892634549878784/813134943118426142/depreson.PNG",
    "https://cdn.discordapp.com/attachments/315892634549878784/813134951099662336/Screenshot_20201109_175539_com.snapchat.android.jpg",
    "https://cdn.discordapp.com/attachments/315892634549878784/813134927209168976/image0.png",
    "https://cdn.discordapp.com/attachments/315892634549878784/813134960206020628/Screenshot_20201115_222838_com.zhiliaoapp.musically.jpg",
    "https://cdn.discordapp.com/attachments/315892634549878784/813134934826418226/IMG_20201016_145824.png",
    "https://cdn.discordapp.com/attachments/310097054426857492/754638612842151936/Snapchat-1991353265.jpg",
    "https://cdn.discordapp.com/attachments/315892634549878784/813135037566156811/kok.png",
    "https://cdn.discordapp.com/attachments/315892634549878784/813135064908169286/bot.jpg",
    "https://cdn.discordapp.com/attachments/821143470654619688/821143499901501470/image0.png",
      ]
    
    await ctx.send(f"{random.choice(filipfotky)}")

@client.command()
async def dolezite(ctx):
    await ctx.send("#rolničky")

@client.command()
async def paket(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/606128960602112003/768742549904687104/PaketPhoenix2.mp4")

@client.command()
async def kpn(ctx, vec):
    veci = ["kameň",
    "papier",
    "nožnice"] 
    vecrandom = f"{random.choice(veci)}"
    
    if vec == "kameň" and vecrandom == "kameň":
        await ctx.send(f"kameň, remíza")
    elif vec == "kameň" and vecrandom == "nožnice":
        await ctx.send(f"nožnice, vyhral si")
    elif vec == "kameň" and vecrandom == "papier":
        await ctx.send(f"papier, prehral si")
    elif vec == "papier" and vecrandom == "papier":
        await ctx.send("papier, remíza")
    elif vec == "papier" and vecrandom == "nožnice":
        await ctx.send("nožnice, prehral si")
    elif vec == "papier" and vecrandom == "kameň":
        await ctx.send("kameň, vyhral si")
    elif vec == "nožnice" and vecrandom == "nožnice":
        await ctx.send("nožnice, remíza")
    elif vec == "nožnice" and vecrandom == "kameň":
        await ctx.send("kameň, prehral si")
    elif vec == "nožnice" and vecrandom == "papier":
        await ctx.send("papier, vyhral si")


@client.command()
async def pravidla(ctx):
    embed = discord.Embed(
        title= "Pravidlá",
        description= "1. pravidal:\nnebuď toxic\nveľmi\nrules:\nV-tuber je bad\namuing us memes= ban\n(nieste vtipny stfu)\nautisticke ear-rapy ktore mi odpalia sluchatka do 69. dimenzie= ban\n<:FeelsSupportMan:668208524412715008>",
        colour= discord.Colour.blue(),
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/606128960602112003/743036789371174912/jajo1.png")
    await ctx.send(embed=embed)

@client.command()
async def jebaited(ctx):
    await ctx.send("https://www.youtube.com/watch?v=d1YBv2mWll0")

@client.command()
async def support(ctx):
    embed2 = discord.Embed(
        title= "Support",
        description= "SUPORT: ak chcete ban abo daco tak piste\nkamaratskyspolok492@gmail.com\ntod: vitko.tom@gmail.com\nbrnkj123: brnkj123@gmail.com\nsinksun: tomasko.jakubec@gmail.com\nextra suppport\nradi pomozeme\n<:FeelsSupportMan:668208524412715008>",
        colour= discord.Colour.purple(),
    )
    embed2.set_image(url="https://www.nabdsys.com/blogs/wp-content/uploads/2015/11/iStock_000034862400Large-2.jpg")
    await ctx.send(embed=embed2)

@client.command()
async def rybar(ctx):
    ryby = ["🐈 catfish",
    "🐟 rybka",
    "🦑 squid pog",
    "🦈 žralok!!! pog",
    "🐬 jej aky pekny delfín",
    "🐋 CRAZY RARE CATCH"
    "🐠 tropical fish :O"
    "🐡 https://www.youtube.com/watch?v=V2H56R1dus0&ab_channel=AngusWu",
    "🐉 dračik"]

    cisla = ["1", "2"]
    

    
    await ctx.send("🎣 chytám ryby")
    cislovyber = random.choice(cisla)
    if cislovyber == "1":
        await ctx.send("rip nic si nechytil")
    elif cislovyber == "2":
        await ctx.send(f"{random.choice(ryby)}")





@client.command()
async def pp(ctx, *, meno):
    dlzka = ["B=D",
    "B==D",
    "B===D",
    "B====D",
    "B======D",
    "B=======D",
    "B=========D",
    "B===========D",
    "B=============D",
    "B∞D"]
    
    await ctx.send(f"{meno} pp: {random.choice(dlzka)}")


@client.command()
async def gay(ctx, *, meno2):
    await ctx.send(f"{meno2} je na {random.randint(0, 100)}% gay")


@client.command()
async def cisielko(ctx, *, cislo):
    cisloplus = float(cislo)
    nula = False
    kladne = False


    if cisloplus == 0:
        await ctx.send("Zadané číslo je 0")
    elif cisloplus >0:
        await ctx.send("Zadané číslo je kladné")
    elif cisloplus <0:
        await ctx.send("Zadané číslo je záporné")

    if cisloplus == 0:
        nula = True


    if (cisloplus % 2) == 0 and nula is False:
        await ctx.send("Zadané čislo je párne")
        kladne = True
    elif kladne is False and nula is False:
        await ctx.send("Zadané číslo je nepárne") 

@client.command()
async def hi(ctx):
    await ctx.send("Ahoj!")

@client.command()
@commands.has_any_role("Staff")
async def staff(ctx):
    await ctx.send("Si staff :)")

@staff.error
async def staff_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("yu no staff kekw")
        



@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount = 5):
    deleted = await ctx.channel.purge(limit=int(ammount))
    await ctx.send("Vymazané {} správy, ktoré už nikto neuvidí".format(len(deleted)))

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Prepáč vyzerá to, že nemáš povolenie na tento príkaz. (manage_messages) :)")


@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    

@client.command()
async def spid(ctx):
    await ctx.send(f"uwu som rýchli {round(client.latency * 1000)}ms pogu")


@client.command()
async def brnkj(ctx):
    await ctx.send("https://www.twitch.tv/brankoj123")





@client.command()
async def weird(ctx):
    images = ["https://www.youtube.com/watch?v=Twv3bEFddNM",
    "https://cdn.discordapp.com/attachments/707526343881130074/722127187100303432/graham-crashes-hed-2016.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722127363520856125/aa6b6c3760973e663d0ac8d85c593cf5.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722127641708200016/cursed-image-mammal.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722127733261336650/86081446-1569859251.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722127976879095849/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128014791671808/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128080638050444/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128121599623289/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128163538206870/85807145.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128242869403693/tumblr_static_tumblr_static_64gyg0zlygsgo0skwgc488cw8_640.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128355066904677/0abb9b4326b23eee7d49009ede9c757c86919dd2r1-280-512v2_hq.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128355066904677/0abb9b4326b23eee7d49009ede9c757c86919dd2r1-280-512v2_hq.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128398796849162/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128476479684639/cursed-image-creepy-simba-scene-with-a-cat.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128543617646712/7f51db4ca8ee839c60a035e84385a2ac.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128585246375946/frclj57p5sg31.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128631010426950/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128688946085998/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128787566886952/839a7a2c-06a9-48ce-a729-c0052ce60254.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128824526962728/Whatexactlymakesanimagecursedihaveseena_b10d304b43cf52b2a608d6a74d50ddab.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128866717597786/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128902088294521/80GeRMz.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722128949559165420/37803505_215388009143524_4193577716735279104_n.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129010842271864/154c69007777e25e675529490444.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129053871636630/Cursed_3-1.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129101560741928/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129150684692600/19-pictures-literally-no-one-on-the-internet-should-be-allowed-to-see-15.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129204740620428/97548446_571345427094283_8583434494119059856_n.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129242430636202/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129406746689556/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129456071835688/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129515962302584/97538653_262814854908981_4183346867751864855_n.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129549470597180/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129588213383188/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722129924517003294/85668697.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130100283244655/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130170873512046/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130396376203404/64add296f4048298c76ce3e377283893.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130586465992826/origin.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130613758328903/300644661340201.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130876086878258/weird-pig.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130943573229608/images.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722130988960055386/367c71d6c561978056603ea5bdbd4370.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722131036930310154/sub-buzz-9885-1538862184-1.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722185379028926474/Like-Your-Manicures-Weird-Then-This-is-the-Instagram-Account-to-Follow.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722185312364789771/weird-kids-youtube.png",
    "https://cdn.discordapp.com/attachments/707526343881130074/722185165660749914/5aaa1cc4c422b-funny-weird-wtf-stock-photos-28-5a3a5b135f099__700.png",
    "https://cdn.discordapp.com/attachments/606128960602112003/725426986859626606/Macintosh_128k_transparency.png"
    ]
    
    await ctx.send(f"{random.choice(images)}")

@client.command()
async def rngveta(ctx):
    member = ctx.message.author

    vecicky = ["slabko",
    "silný",
    "gei",
    "fukár",
    "radiator",
    "feťák",
    "neviem",
    "feťák dušan",
    "uga buga"
    ]
    await ctx.send(f"{member} je {random.choice(vecicky)}.")


@client.command()
async def calculate(ctx, num1, operacia ,num2):
    if operacia == "*":
        await ctx.send(float(num1) * float(num2))
    elif operacia == "+":
        await ctx.send(float(num1) + float(num2))
    elif operacia == "/":
        await ctx.send (float(num1) / float(num2))
    elif operacia == "-":
        await ctx.send(float(num1) - float(num2))
    
    
@client.command()
async def telefon(ctx):
    embedtel = discord.Embed(
        title= "Telefón",
        description= "tut: 0915 494 688\nAdam: 0944 363 993 \nFilip: 0915 610 520\nBraňo: 0944 629 565\nAndrej: 0907 721 450\nPotato: 0903 935 990\n Dušan: 0902 070 044\n Panda: 0902 442 229\n Mirka: 0903 350 905\n Maťo: 0917 726 700\n Sima: 0948 620 044\n Tamara: 0908 333 277\n Peťa: 0949 222 967\n Šimon: 0944 897 008",
        colour= discord.Colour.blue(),
    )
    embedtel.set_image(url="https://cdn.discordapp.com/attachments/606128960602112003/774980744170569738/unknown.png")
    await ctx.send(embed=embedtel)


@client.command()
async def ban(ctx):
    await ctx.send("chceš")



@client.command()
async def rng(ctx, num1r, num2r):
    await ctx.send(f"Tu máš číslo z neba: {random.randint(int(num1r), int(num2r))}")

@client.command()
async def L(ctx):
    await ctx.send("Si ty HAHAHAH")

@client.command()
async def god(ctx, *, question):
    responses = ["Na 100 parcent",
                 "Určite",
                 "Možno",
                 "Skôr nie",
                 "Nie",
                 "Určite nie",
                 "gei"]
    await ctx.send(f"Otázočka: {question}\nOdpoveď od boha: {random.choice(responses)}")



@client.command()
async def sirena(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/435938425196249108/717827879156842538/siren_dance.mp4")



@client.command()
async def rockefel(ctx):
    await ctx.send("https://www.youtube.com/watch?v=hjGZLnja1o8")


@client.command()
async def n2(ctx, num1n2):
    num1n2v = float(num1n2) * float(num1n2)
    await ctx.send(f"{num1n2v}")

@client.command()
async def sq(ctx, numsq, sqnum):
    numsqfloat = float(numsq)
    sqnumfloat = float(sqnum)
    numsq1 = numsqfloat**sqnumfloat
    await ctx.send(f"{numsq1}")



client.run("NzAyOTc2NzU2Nzk3MTQ1MTE4.XtkDtw.sihSFjNieF1notPBTc6zkZpjLQ0")