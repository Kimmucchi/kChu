import os, re, json, asyncio, traceback, datetime, math, pytz, time
import pymongo
import discord
from io import BytesIO
from discord.ext import commands, tasks

#GLOBAL VARIABLES
mongo = pymongo.MongoClient('mongodb+srv://rk:tc@cluster0.29x6p.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
database = mongo['leaderboard']
collection = database['contestants']

class EventLeaderboard(commands.Cog):
  def __init__(self, bot):
    print("Initiated WTG Leaderboard")
    self.bot = bot

#--------------------------------------------------
#HELP
  @commands.command(name='eventhelp', aliases=['ehelp'])
  async def ehelp(self,ctx):
    embed = discord.Embed(color=9693439, title='Event Commands', description='• `c/lb`\n> Shows the top scoring players!\n\n• `c/points <@user> <amount>` \n> Gives a specified amount of points.\n\n• `c/deduct <@user> <amount>`\n> Subtracts a specified amount of points.\n\n• `c/find <@user>`\n> Looks for a specific user\'s details.')
    await ctx.send(embed=embed)
#--------------------------------------------------
#LEADERBOARD
  @commands.command(name='leaderboard', aliases = ['lb'])
  async def leaderboard(self, ctx):
    def leaderboard_embed(description):
      embed = discord.Embed(color=9693439, title='LEADERBOARD', description=description)
      embed.set_image(url='https://i.ibb.co/sFdTmxb/smalldivider.png')
      embed.set_author(name="Week #2")
      embed.set_footer(text='Who\'s That Genshinmon(?)')
      embed.set_thumbnail(url='https://i.ibb.co/X5C8Bfb/wtg.png')
      return embed

    embed_str = ""
    rank = 0
    current = 0
    buttons = [u'\u23EA', u'\u25C0', u'\u25B6', u'\u23E9']
    pages = []
    for x in collection.find().sort("points", -1):
      member = ctx.guild.get_member(int(x["UID"]))
      rank += 1
      new_line = f'`{rank}.` {member.mention}\n> **SCORE**: `{str(x["points"])}`\n'
      embed_str += new_line
      new_page = rank%5
      if new_page == 0:
        pages.append(embed_str)
        embed_str = ""
    if embed_str != "":
      pages.append(embed_str)
    msg = await ctx.channel.send(embed=leaderboard_embed(pages[current]))
    while True:
      for button in buttons:
        await msg.add_reaction(button)
      try:
        reaction, user = await self.bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)
      except asyncio.TimeoutError:
        await ctx.send('*Timed out.*')
        await msg.clear_reactions() 
        break
      else:
        previous_page = current
        if reaction.emoji == u'\u23EA':
          current = 0
        elif reaction.emoji == u'\u25C0':
          if current > 0:
            current -= 1
        elif reaction.emoji == u'\u25B6':
          if current < len(pages)-1:
            current += 1
        elif reaction.emoji == u'\u23E9':
          current = len(pages)-1
        for button in buttons:
          await msg.remove_reaction(button, ctx.author)
        if current != previous_page:
          await msg.edit(embed=leaderboard_embed(pages[current]))

#--------------------------------------------------
  #ADD POINT
  @commands.command(name='points')
  @commands.has_role('Cicin Mage | EVENT')
  async def points(self, ctx, member: discord.Member, amt=1):
    channel = self.bot.get_channel(864278616807571496)
    #from ctx get author info
    contestant = member.name
    UID = str(member.id)
    #determine whether or not the member already exists in the database:
    find = collection.find_one({"UID": UID})
    if find is None:
      member = ctx.guild.get_member(member.id)
      #prepare data for leaderboard column
      dictionary = {"name": contestant, "UID": UID, "points": amt}
      #insert data into leaderboard column
      x = collection.insert_one(dictionary)
      await ctx.send(f'+{str(amt)} added to {contestant}')
      embed = discord.Embed(color=3066993, description=f'{ctx.author.mention} added {amt} to {member.mention}\'s score!')
      await channel.send(embed=embed)
    elif find["UID"] == UID:
      member = ctx.guild.get_member(int(find["UID"]))
      find_points = {"UID": UID}
      new_points = {"$set":{"points": find["points"]+amt}}
      collection.update_one(find_points, new_points)
      await ctx.send(f'+{str(amt)} added to {contestant} [Updated]')
      embed = discord.Embed(color=3066993, description=f'{ctx.author.mention} added {amt} to {member.mention}\'s score!')
      await channel.send(embed=embed)
  @points.error
  async def points_error(self, ctx, error):
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send('Only **Cicin Mages** can use this command!')
    

#REMOVE POINT
  @commands.command(name='deduct')
  @commands.has_role('Cicin Mage | EVENT')
  async def deduct(self, ctx, member: discord.Member, amt=1):
    channel = self.bot.get_channel(864278616807571496)
    #from ctx get author info
    contestant = member.name
    UID = str(member.id)
    #prepare data for leaderboard column
    dictionary = {"name": contestant, "UID": UID, "points": 1}
    #determine whether or not the member already exists in the database:
    find = collection.find_one({"UID": UID})
    if find is None:
      return
    elif find["UID"] == UID:
      member = ctx.guild.get_member(int(find["UID"]))
      find_points = {"UID": UID}
      new_points = find["points"]-amt
      if new_points < 0:
        new_points = 0
      update_points = {"$set":{"points": new_points}}
      collection.update_one(find_points, update_points)
      await ctx.send(f'-{amt} subtracted from {contestant}\'s score [Updated]')
      embed = discord.Embed(color=15548997, description=f'{ctx.author.mention} subtracted {amt} from {member.mention}\'s score!')
      await channel.send(embed=embed)
  @deduct.error
  async def points_error(self, ctx, error):
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send('Only **Cicin Mages** can use this command!')

#FIND USER'S POINT
  @commands.command(name='find')
  async def find(self, ctx, member:discord.Member):
  #from ctx get author info
    try:
      contestant = member.name
      UID = str(member.id)
      x = collection.find_one({"UID": UID})
      embed = discord.Embed(color=9693439, title=member.nick, description=f'__**Profile**__\n•{member.mention}\n\n__**User ID**__ \n•`{x["UID"]}` \n\n__**Points**__\n•{x["points"]}')
      embed.set_author(name=f'{member.name}#{member.discriminator}')
      await ctx.send(embed=embed)
    except:
      await ctx.send('*This user is not on the leaderboard.*')

def setup(bot):
  bot.add_cog(EventLeaderboard(bot))