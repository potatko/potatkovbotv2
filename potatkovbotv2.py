import discord
import random
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
async def pravidla(ctx):
    await ctx.send("1. Nehraj Fortnite(Perma-ban\n2. NEHRAJ GROWTOPIU (BAN)\n3. NEBUD RASISTICKY iba joky su povolené (KICK)\n4. DUSAN JE BOT (KICK)\n5. POTATO NEVIE NIC (PERMA-BAN)\n6.NEMENTE VECI (NIC)\n7.DUSAN VYMYSLEL ROLNICKY (TO NENI PRAVDA)\n8.POTATO- MA DVOJNIKA (TRUE)\n9.TOMAS JE DLHO OBED(30MINUT)\n10.VSETCI SME BOTI OKREM POTATA(lebo dal misiu)\n11.NEVYMSLAJ SI (PERMA-BAN)\nAK MATE PROBLEM NAPISTE NAM NA 24/7 SUPPORT: kamaratskyspolok492@gmail.com \:FeelsSupportMan:")

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
        await ctx.send("Prepáč vyzerá to, že nemáš povolenie na tento príkaz. :)")


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