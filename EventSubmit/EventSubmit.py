import os, re, json, asyncio, traceback, datetime, math, pytz, time
import discord
from io import BytesIO
from discord.ext import commands, tasks

class EventSubmit(commands.Cog):
  def __init__(self, bot):
    print("initiated cog")
    self.bot = bot
    self.ctx = None

#------------------------------------------------
  def legend(self, emoji):
    if emoji == "🟦":
      color = 20223
    elif emoji == "🟪":
      color = 8408499
    elif emoji == "🟩":
      color = 518412
    return color

  @commands.Cog.listener()
  async def on_message(self, message):
      def check(reaction, user):
        return user != self.bot.user
      def not_bot(msg):
        return user != self.bot.user and message.author == msg.author
      if message.author.id not in self.bot.sent_event_message:
        # Checking if its a dm channel
        if not message.guild:
          # Getting the channel
          channel = self.bot.get_channel(855659470456619008)

          if not message.author.bot:
            try:
              #ask user to react accordingly
              embed = discord.Embed(color=11534335, title="Hello, cutie~! Did ya need anything?", description="`✅` —  Yes, I'd like to participate in an event!\n `❌` — Nope!")
              cicin = await message.channel.send(embed=embed)
              self.bot.sent_event_message.append(message.author.id)
              await cicin.add_reaction("✅")
              await cicin.add_reaction("❌")
            
            #WAITING FOR A REACTION FROM THE USER HERE
              reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
              #print(reaction, user)

            #reaction results
              if reaction.emoji == "✅":
                embed = discord.Embed(color=11534335, title="Active Events List", description="`🟦` — Signora Emoji\n `🟪` — Signora Icon \n `🟩` — Signora Banner")
                cicin = await message.channel.send(embed=embed)
                await cicin.add_reaction("🟦")
                await cicin.add_reaction("🟪")
                await cicin.add_reaction("🟩")
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                embed_color = self.legend(reaction.emoji)
            #COLOR SELECT
                embed = discord.Embed(color=embed_color, title="Please Read", description="Rules rules blah blah yada yada wee woo~\n`✅` —  Agree\n `❌` — No, thank you.")
                cicin = await message.channel.send(embed=embed)
                await cicin.add_reaction("✅")
                await cicin.add_reaction("❌")
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                if reaction.emoji == "✅":
                  embed = discord.Embed(color=embed_color, title="Please Submit Your Entry Now:", description="Upload your image here or paste the image URL here.\n> If you are using an image URL, please make sure that it ends in \n> `.jpg/jpeg, .png, or .gif` or your entry will be invalidated.")
                  await message.channel.send(embed=embed)
                  entry = await self.bot.wait_for("message", timeout=60.0, check=not_bot)
                  #attachment = await self.bot.wait_for(Attachment, timeout=30.0, check=not_bot)
                #LENGTH OF SUBMISSION != 0
                  print("DEBUG", entry.content)
                  if len(entry.content) != 0:
                    #await message.channel.send(f"```{entry.content}```")
                    embed = discord.Embed(title="Would you like to say anything to the staff?")
                    cicin = await message.channel.send(embed=embed)
                    await cicin.add_reaction("✅")
                    await cicin.add_reaction("❌")
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                    if reaction.emoji == "✅":
                      embed = discord.Embed(title="What would you like to say?")
                      await message.channel.send(embed=embed)
                      user_description = await self.bot.wait_for("message", timeout=30.0, check=not_bot)
                      try:
                        embed = discord.Embed(color=embed_color, title=f"{entry.author} | `{entry.author.id}`", description=f"`Author`: {user_description.content}")
                        embed.set_image(url=entry.content)
                        embed.set_footer(text="Embed Color: 🟦—Emoji | 🟪—Icon | 🟩—Banner")
                        await channel.send(embed=embed)
                        await message.channel.send("*Your submission has been sent to the staff!*\n**Here is your receipt:**", embed=embed)
                      except:
                        embed = discord.Embed(color=11014160, title=f"`Your Entry Is Invalid! (｡•́︿•̀｡)`", description=f"**READ THESE INSTRUCTIONS CAREFULLY AND DM ME AGAIN!**\nYou must upload your image or paste the image URL when I ask you to!\n> __If you are using an image URL, please make sure that it ends in__ \n> `.jpg/jpeg, .png, or .gif` __or your entry will be invalidated!!__")
                        await message.channel.send(embed=embed)
                    if reaction.emoji == "❌":
                      try:
                        embed = discord.Embed(color=embed_color, title=f"{entry.author} | `{entry.author.id}`")
                        embed.set_image(url=entry.content)
                        embed.set_footer(text="Embed Color: 🟦—Emoji | 🟪—Icon | 🟩—Banner")
                        await channel.send(embed=embed)
                        await message.channel.send("*Your submission has been sent to the staff!*\n**Here is your receipt:**", embed=embed)
                      except:
                        embed = discord.Embed(color=11014160, title=f"`Your Entry Is Invalid! (｡•́︿•̀｡)`", description=f"**READ THESE INSTRUCTIONS CAREFULLY AND DM ME AGAIN!**\nYou must upload your image or paste the image URL when I ask you to!\n> __If you are using an image URL, please make sure that it ends in__ \n> `.jpg/jpeg, .png, or .gif` __or your entry will be invalidated!!__")
                        embed.set_footer(text = "Your submission did not reach the staff.")
                        await message.channel.send(embed=embed)
                #ATTACHMENTS
                  if user != self.bot.user and not message.guild:  
                    #files = []
                    for file in entry.attachments:
                      #fp = BytesIO()
                      #await file.save(fp)
                      #files.append(discord.File(fp, filename=file.filename, spoiler=file.is_spoiler()))
                    #await message.channel.send(files=files)
                      embed = discord.Embed(title="Would you like to say anything to the staff?")
                      cicin = await message.channel.send(embed=embed)
                      await cicin.add_reaction("✅")
                      await cicin.add_reaction("❌")
                      reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                      if reaction.emoji == "✅":
                        embed = discord.Embed(title="What would you like to say?")
                        await message.channel.send(embed=embed)
                        user_description = await self.bot.wait_for("message", timeout=30.0, check=not_bot)
                        try:
                          embed = discord.Embed(color=embed_color, title=f"{entry.author} | `{entry.author.id}`", description=f"`Author`: {user_description.content}")
                          embed.set_image(url=file.url)
                          embed.set_footer(text="Embed Color: 🟦—Emoji | 🟪—Icon | 🟩—Banner")
                          await channel.send(embed=embed)
                          await message.channel.send("*Your submission has been sent to the staff!*\n**Here is your receipt:**", embed=embed)
                        except:
                          embed = discord.Embed(color=11014160, title=f"`Your Entry Is Invalid! (｡•́︿•̀｡)`", description=f"**READ THESE INSTRUCTIONS CAREFULLY AND DM ME AGAIN!**\nYou must upload your image or paste the image URL when I ask you to!\n> __If you are using an image URL, please make sure that it ends in__ \n> `.jpg/jpeg, .png, or .gif` __or your entry will be invalidated!!__")
                          await message.channel.send(embed=embed)
                      if reaction.emoji == "❌":
                        try:
                          embed = discord.Embed(color=embed_color, title=f"{entry.author} | `{entry.author.id}`")
                          embed.set_image(url=file.url)
                          embed.set_footer(text="Embed Color: 🟦—Emoji | 🟪—Icon | 🟩—Banner")
                          await channel.send(embed=embed)
                          await message.channel.send("*Your submission has been sent to the staff!*\n**Here is your receipt:**", embed=embed)
                        except:
                          embed = discord.Embed(color=11014160, title=f"`Your Entry Is Invalid! (｡•́︿•̀｡)`", description=f"**READ THESE INSTRUCTIONS CAREFULLY AND DM ME AGAIN!**\nYou must upload your image or paste the image URL when I ask you to!\n> __If you are using an image URL, please make sure that it ends in__ \n> `.jpg/jpeg, .png, or .gif` __or your entry will be invalidated!!__")
                          embed.set_footer(text = "Your submission did not reach the staff.")
                          await message.channel.send(embed=embed)
                  elif reaction.emoji == "❌":
                    embed = discord.Embed(color=11014160, title="Alright then, see you around~ ♫")
                    await cicin.edit(embed=embed)  
            except asyncio.exceptions.TimeoutError:
              print("timeout error")
              self.bot.sent_event_message.remove(message.author.id)
              embed = discord.Embed(color=11014160, title="Alright then, see you around~ ♫")
              embed.set_footer(text = "Your request has timed out! Please try again.")
              await cicin.edit(embed=embed)
            else:
              print("success!")
              self.bot.sent_event_message.remove(message.author.id)
#------------------------------------------------
def setup(bot):
    bot.add_cog(EventSubmit(bot))