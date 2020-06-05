import discord
import random
from discord.ext import commands



client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Ideme na to :)")

@client.event
async def on_member_join(member):
    print(f"{member} zavítal na Kamarátsky spolok vitaj degeš")

@client.event
async def on_member_remove(member):
    print(f"{member} vypadol het F in a chat")

@client.command()
async def jebaited(ctx):
    await ctx.send("https://www.youtube.com/watch?v=d1YBv2mWll0")

@client.command()
async def clear(ctx, ammount = 5):
    deleted = await ctx.channel.purge(limit=int(ammount))
    await ctx.send("Vymazané {} správy, ktoré už nikto neuvidí".format(len(deleted)))

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
    await ctx.send("https://www.youtube.com/watch?v=hjGZLnja1o8\n-play rockefeller street nightcore")






client.run("NzAyOTc2NzU2Nzk3MTQ1MTE4.XtkDtw.sihSFjNieF1notPBTc6zkZpjLQ0")