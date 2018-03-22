import discord
import asyncio
from discord.ext.commands import Bot
from discord import MessageType
import random, pickle, codecs, urllib.request
import logging
from datetime import datetime

jd = Bot(command_prefix="!")

@my_bot.event
async def on_message(ctx):
    print(ctx.content)
    words = {"ayy":"lmao","wew":"lad","ba dum":"tss","ur gay":"no u","he's a big guy":"For you."}
    content = ctx.content.lower()
    s = ctx.content.lower().replace(" ","")
    if content.replace(" ","") in [i.replace(" ","") for i in words]:
        await ctx.channel.send(words[content])
    await my_bot.process_commands(ctx)

#Roll 1-100
@my_bot.command()
async def roll(ctx,limit = 101):
    num = str(random.randrange(1,limit))
    if len(num) > 1 and num[-1] == num[-2]:
        return await ctx.channel.send(num+"\nChecked!")
    else: return await ctx.channel.send(num)




jd.run("MzA3OTczNzA5NzMyMzgwNjgz.C-aGZQ.t5sUMslgA2zejllPmW_0HBt4Yng")
