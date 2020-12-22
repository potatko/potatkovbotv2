import math
import discord
import random
import shutil
import asyncio
import os
from discord.ext import commands
from discord.utils import get




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
    filipfotky = ["https://media.discordapp.net/attachments/606128960602112003/754640136209432607/filip_tvar.png?width=1202&height=676",
    "https://cdn.discordapp.com/attachments/606128960602112003/754639698437341244/filip.png",
    "https://cdn.discordapp.com/attachments/606128960602112003/738472030587846751/Screenshot_20200730_220357_com.discord.jpg",
    "https://cdn.discordapp.com/attachments/606128960602112003/735203285211807855/0IuBsG_qKU6Pf3yf2YpbYw_0_0.png",
    "https://cdn.discordapp.com/attachments/310097054426857492/744589199444803594/IMG_20200816_190141.jpg",
    "https://cdn.discordapp.com/attachments/310097054426857492/754638612842151936/Snapchat-1991353265.jpg"  ]
    
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
        description= "1. :)\nAK MATE PROBLEM NAPISTE NAM NA 24/7 SUPPORT: kamaratskyspolok492@gmail.com <:FeelsSupportMan:668208524412715008>",
        colour= discord.Colour.blue(),
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/606128960602112003/743036789371174912/jajo1.png")
    await ctx.send(embed=embed)

@client.command()
async def jebaited(ctx):
    await ctx.send("https://www.youtube.com/watch?v=d1YBv2mWll0")


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


@client.command(pass_context=True)
@commands.has_any_role("DJ")
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"Pripojil som sa do {channel}")

@join.error
async def join_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("Prepáč vyzerá to, že nemáš povolenie na tento príkaz. (DJ) :)")

@client.command(pass_context=True)
@commands.has_any_role("DJ")
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send (f"Odpojil som sa z {channel}")

@leave.error
async def leave_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("Prepáč vyzerá to, že nemáš povolenie na tento príkaz. (DJ) :)")

    

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
        description= "tut: 0915 494 688\nAdam: 0944 363 993 \nFilip: 0915 610 520\nBraňo: 0944 629 565\nAndrej: 0907 721 450\nPotato: 0903 935 990\n Dušan: 0902 070 044\n Panda: 0902 442 229\n Mirka: 0903 350 905\n Maťo: 0917 726 700\n Sima: 0948 620 044\n Tamara: 0908 333 277\n Peťa: 0949 222 967",
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