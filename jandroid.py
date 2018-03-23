import discord
import asyncio
from discord.ext.commands import Bot
from discord import MessageType
import random, pickle, codecs, urllib.request
import logging
from datetime import datetime

from xp_db import *

jd = Bot(command_prefix="!")
my_bot.remove_command("help")

@jd.event
async def on_message(ctx):
    user_id = ctx.author.id
    content = ctx.content.lower()

    #ROLL
    if content == "roll":
        roll_lim = 100
        num = str(random.randrange(1,roll_lim))
        if len(num) > 1 and num[-1] == num[-2]:
            return await ctx.channel.send(num+"\nChecked!")
        else: return await ctx.channel.send(num)
    elif content[:4] == "roll":
        try:
            roll_lim = int(content.split(" ")[1])
            num = str(random.randrange(1,roll_lim))
            if len(num) > 1 and num[-1] == num[-2]:
                return await ctx.channel.send("{} \n**Checked!**".format(num))
            else: return await ctx.channel.send(num)
        except ValueError:
            pass

    gangs_owners = [i[2] for i in gen_dump("gang_xp")]

    elif content == "make_gang":
        def create_gang(gang_name):
            return ctx.guild.create_gang(name)
        
        words = content.split(" ")
        if len(words) > 1:
            role_name = " ".join(words)
            new_role = create_gang(content)
            role.id = new_role.id
            members = (i[0] for i in gen_dump("membership"))
            owners = (i[2] for i in gen_dump("gang_xp"))

        pass

    elif content == "join_gang":
        pass

    elif content == "leave_gang":
        pass

    await jd.process_commands(ctx)

@jd.event
async def on_ready():
    print("READY!")




jd.run("MzA3OTczNzA5NzMyMzgwNjgz.C-aGZQ.t5sUMslgA2zejllPmW_0HBt4Yng")
