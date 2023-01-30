import discord
from discord.ext import commands
from random import choice
import os

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.event
async def on_ready():
	print(f"---<= Logged In As: {bot.user} =>---")


@bot.event
async def on_member_join(member):
	channel = bot.get_channel(1065348602123259965)
	message_versions = ['your journey has just begun', 'we hope you enjoy your stay', 'we know that your brilliance will contribute greatly to the growth of our community', 'we hope you’ll grow with us']
	embed = discord.Embed(
		title=f"🎉 Member.add() 🎉",
		description=f"Welcome {member.mention}, {choice(message_versions)}!",
		color=discord.Colour.green()
	)
	await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
	channel = bot.get_channel(1066048757742968932)
	message_versions = ['gave up on their journey', 'was yeeted and defeated (╯°□°）╯︵ ┻━┻', 'is no longer with us ', 'just gave up ¯\\_(ツ)_/¯']
	embed = discord.Embed(
		title=f"☹ Member.remove() ☹",
		description=f"{member.mention} {choice(message_versions)}.",
		color=discord.Colour.red()
	)
	await channel.send(embed=embed)


bot.run(os.getenv("BOT_TOKEN"))
