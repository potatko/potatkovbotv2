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
async def pravidla(ctx):
    embed = discord.Embed(
        title= "Pravidlá",
        description= "1. Nehraj Fortnite(Perma-ban)\n2. NEHRAJ GROWTOPIU (BAN)\n3. NEBUD RASISTICKY iba joky su povolené (KICK)\n4. DUSAN JE BOT (KICK)\n5. POTATO NEVIE NIC (PERMA-BAN)\n6.NEMENTE VECI (NIC)\n7.DUSAN VYMYSLEL ROLNICKY (TO NENI PRAVDA)\n8.POTATO- MA DVOJNIKA (TRUE)\n9.TOMAS JE DLHO OBED(30MINUT)\n10.VSETCI SME BOTI OKREM POTATA(lebo dal misiu)\n11.NEVYMSLAJ SI (PERMA-BAN)\nAK MATE PROBLEM NAPISTE NAM NA 24/7 SUPPORT: kamaratskyspolok492@gmail.com <:FeelsSupportMan:668208524412715008>",
        colour= discord.Colour.blue(),
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/606128960602112003/719836984276680844/pravidla-300x300.png")
    await ctx.send(embed=embed)

@client.command()
async def jebaited(ctx):
    await ctx.send("https://www.youtube.com/watch?v=d1YBv2mWll0")

@client.command()
@commands.has_any_role("Staff", "Moooover")
async def clear(ctx, ammount = 5):
    deleted = await ctx.channel.purge(limit=int(ammount))
    await ctx.send("Vymazané {} správy, ktoré už nikto neuvidí".format(len(deleted)))

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("Prepáč vyzerá to, že nemáš povolenie na tento príkaz. (STAFF) :)")


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
async def spoiler(ctx):
    await ctx.send("duskov pc je slabý")

@client.command()
async def potato(ctx):
    await ctx.send("je frajer")

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
async def calculate(ctx, num1, num2, operacia):
    if operacia == "*":
        await ctx.send({num1} * {num2} )
    elif operacia == "+":
        await ctx.send({num1} + {num2})
    elif operacia == "/":
        await ctx.send ({num1} / {num2})
    elif operacia == "-":
        await ctx.send({num1} - {num2})
    
    



@client.command()
async def ban(ctx):
    await ctx.send("chceš")



@client.command()
async def rng(ctx):
    await ctx.send(f"Tu máš číslo z neba: {random.randint(1, 5)}")

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





client.run("NzAyOTc2NzU2Nzk3MTQ1MTE4.XtkDtw.sihSFjNieF1notPBTc6zkZpjLQ0")