import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import os
import sys
import traceback


BOT_PREFIX = ("yes")


client = Bot(command_prefix=BOT_PREFIX)
c2 = discord.Client()

async def on_ready():
    await client.change_presence(game=Game(name="Go fuck yourself!"))
    print("Logged in as " + client.user.name)


@client.command(pass_context=True)
async def counter(ctx):
    embed = discord.Embed(title="Counter", description="Server info", color=0x6FA8DC)
    embed.add_field(name="Name", value=ctx.message.guild.name)
    embed.add_field(name="Owner", value=ctx.message.guild.owner.mention)
    embed.add_field(name="Members", value=ctx.message.guild.member_count)
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    await client.say(embed=embed)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.command()
async def double(number):
    squared_value = int(number) + int(number)
    await client.say(str(number) + " x2 is " + str(squared_value))


@client.command(pass_context = True)
@commands.has_permissions(kick_members = True) 
async def kick(ctx, userName: discord.User):
    await client.kick(userName)
    await client.say("sucessfully kicked, sir!")

@client.command(pass_context = True)
@commands.has_permissions(ban_members = True) 
async def ban(ctx, userName: discord.User):
    await client.ban(userName)
    await client.say("sucessfully banned, sir!") 

@client.command()
async def say(*,message):
         await client.say(message)


@client.command(pass_context=True)
async def ping(ctx):
    resp = await client.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await client.edit_message(resp, 'Pong! That took {:.1f}ms.'.format(1000*diff.total_seconds()))


@client.command(pass_context=True,hidden=True,aliases = ["state"])
async def status(ctx,*,message):
    if ctx.message.author.id == '647428003319775245':
         await client.change_presence(game=Game(name= message))
         await client.say("`successfully changed presence`")
    else:
        await client.say("You don't own me!")


@client.command(pass_context=True, hidden=True)
async def stdown(ctx):
    channel = discord.Object(id='755435086043807887')
    if ctx.message.author.id == '647428003319775245':
        await client.say("shutting down...")
        await client.logout()
    else:
        await client.say("You don't have the permission to do this!!!!")
        print(ctx.message.author, "tried to shut me down!")
        await client.send_message(channel, "{} tried to shut me down!!!".format(ctx.message.author))




@client.command(pass_context=True, hidden=True)
async def load(ctx,extension_name : str):
    if ctx.message.author.id == '647428003319775245':
        try:
            client.load_extension(extension_name)
            await client.say("`{} loaded.`".format(extension_name))
        except (AttributeError, ImportError) as e:
            await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
    else:
        await client.say("I wont let YOU do this")

@client.command(pass_context=True,hidden=True)
async def unload(ctx,extension_name : str):
    if ctx.message.author.id == '647428003319775245':
        client.unload_extension(extension_name)
        await client.say("`{} unloaded.`".format(extension_name))
    else:
        await client.say("Reporting you for trying to unload {}".format(extension_name))

@client.command(pass_context=True,hidden=True)
async def reload(ctx,extension_name : str):
    if ctx.message.author.id == '647428003319775245':
        client.unload_extension(extension_name)
        try:
            client.load_extension(extension_name)
            await client.say("`{} reloaded.`".format(extension_name))
        except (AttributeError, ImportError) as e:
            await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
    else:
        await client.say("You can't reload cogs, because you are you.")


@client.command()
async def USRS():
    usrs = list(client.get_all_members())
    await client.say(len(usrs))

@client.command(pass_context = True)
async def clear(ctx, number):
    if ctx.message.author.server_permissions.administrator:
        mgs = []
        number = int(number)
        async for x in client.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await client.delete_messages(mgs)
    else:
        await client.say("you don't have the permissions to do that")


@client.command(pass_context = True, hidden = True)
async def sayd(ctx,*,message):
	await client.delete_message(ctx.message)
	await client.say(message)



        
@cleint.command(pass_context=True)
async def info(ctx,member: discord.Member=None):
    'Show info about a member'
    if member is None:
        member = ctx.message.author
    em = discord.Embed(color=0x00ff00)
    em.add_field(name='Name', value='{0.name}'.format(member))
    em.add_field(name='ID', value='{0.id}'.format(member))
    em.add_field(name='Top Role', value='{0.top_role}'.format(member))
    em.add_field(name='Roles', value=', '.join(g.name for g in member.roles))
    em.add_field(name='Joined', value='{0.joined_at}'.format(member))
    em.set_thumbnail(url=member.avatar_url)
    await client.say(embed=em)

@client.event
async def on_message(message):
	fucks = [
	"Did you mean to say ***fuck***, you fucking piece of family-freindly shit?",
	"just say ***fuck***",
	"JUST SAY FUCK YOU SON OF A BITCH",]
	if ("frick", "f***","f*ck","fck","fok") in message:
		client.say(random.choice(fucks))



client.run(os.getenv("TOKEN"))
