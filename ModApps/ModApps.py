import os, re, json, asyncio, traceback, datetime, math, pytz, time
import discord
from io import BytesIO
from discord.ext import commands, tasks

class ModApps(commands.Cog):
  def __init__(self, bot):
    print("initiated cog")
    self.bot = bot
    self.ctx = None
    self.bot.sent_event_message = []

#------------------------------------------------
#
  def legend(self, emoji):
    if emoji == "๐ฆ":
      color = 20223
    elif emoji == "๐ช":
      color = 8408499
    elif emoji == "๐ฉ":
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
          channel = self.bot.get_channel(840432139790057483)

          if not message.author.bot:
            try:
              #ask user to react accordingly
              embed = discord.Embed(color=11534335, title="Nyan! Nya nya nyaaaan?", description="โโโโโ ๐ฆ โโโโโ\n โข **Cicin Mage | EVENT** \nโ  Yes, I\\'d like to be part of the __Event Staff__!\n\nโโโโโ ๐ โโโโโ\n โข **Fatui Bouncer | NSFW MOD**\nโ  Yes, I\\'d like to be an __NSFW moderator__!\n\nโโโโโ ๐ฑ โโโโโ\n โข **โฝแถ แตแตแตแถฆโพ | Staff**\nโ  Yes, I\\'d like to apply for all open positions!\n\nโโโโโ  โ โโโโโ\n โ **Nope!**")
              embed.set_footer(text='๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: "๐ญโ๐ชโ๐พโ, ๐ฒโ๐พโ ๐ฒโ๐ดโ๐ฒโ ๐ฎโ๐ธโ ๐ญโ๐ฎโ๐ทโ๐ฎโ๐ณโ๐ฌโ ๐ซโ๐ดโ๐ทโ ๐ธโ๐นโ๐บโ๐ซโ๐ซโ! ๐ฉโ๐ดโ ๐พโ๐ดโ๐บโ ๐ผโ๐ฆโ๐ณโ๐นโ ๐นโ๐ดโ ๐ฆโ๐ตโ๐ตโ๐ฑโ๐พโ๐พโ๐พโ๐พโ๐พโ?"')
              cat = await message.channel.send(embed=embed)
              self.bot.sent_event_message.append(message.author.id)
              await cat.add_reaction("๐ฆ")
              await cat.add_reaction("๐")
              await cat.add_reaction("๐ฑ")
              await cat.add_reaction("โ")
            
            #WAITING FOR A REACTION FROM THE USER HERE
              reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
              #print(reaction, user)

            #reaction results
#CICIN MAGE            
              if reaction.emoji == "๐ฆ":
                embed = discord.Embed(color=11534335, title = "Nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *How old are you?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=60.0, check=not_bot)
                age = response.content

                embed = discord.Embed(color=11534335, title = "Nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your timezone?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=60.0, check=not_bot)
                timezone = response.content

                embed = discord.Embed(color=11534335, title = "Nyan, nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Tell us about yourself, so we can get to know you better.*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=1200.0, check=not_bot)
                about_yourself = response.content

                embed = discord.Embed(color=11534335, title = "Nyan? Nya nyan nya nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your schedule like? How much time are you going to contribute?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                schedule = response.content

                embed = discord.Embed(color=11534335, title = "Nyan nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Do you have any previous experience in handling events?*")
                cat = await message.channel.send(embed=embed)
                await cat.add_reaction("โ")
                await cat.add_reaction("โ")
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                if reaction.emoji == "โ":
                  embed = discord.Embed(color=11534335, title = "Nyaan nya nya!", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Please tell us more about them!*")
                  await message.channel.send(embed=embed)
                  response = await self.bot.wait_for('message', timeout=1200.0, check=not_bot)
                  experience = response.content
                elif reaction.emoji == "โ":
                  embed = discord.Embed(color=11534335, title = "Nyaan nya nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What can you contribute to the event team?*")
                  await message.channel.send(embed=embed)
                  response = await self.bot.wait_for('message', timeout=1200.0, check=not_bot)
                  experience = response.content

                embed = discord.Embed(color=11534335, title = "Nyan, Signora-sama nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your opinion of our Queen, Lady Signora?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                signora = response.content
                #SEND EMBED TO CHANNEL
                #FIRST EMBED
                embed1 = discord.Embed(color=discord.Colour(0x0ab6ff), title=f"USER ID: `{response.author.id}`",
                description=f"**AGE**\n__How old are you?__\n```{age}```\n\n**TIMEZONE**\n__What is your timezone?__\n```{timezone}```")
                embed1.set_author(name=f'{response.author}')
                embed1.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed1)
                await asyncio.sleep(1)
                #ABOUT YOURSELF
                embed2 = discord.Embed(color=discord.Colour(0x0ab6ff), title=f"ABOUT ME",
                description=f"\n__Tell us about yourself, so we can get to know you better.__\n```{about_yourself}```")
                embed2.set_author(name=f'{response.author}')
                embed2.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed2)
                await asyncio.sleep(1)
                #SCHEDULE
                embed3 = discord.Embed(color=discord.Colour(0x0ab6ff), title=f"SCHEDULE",
                description=f"\n__What is your schedule like? How much time are you going to contribute?__\n```{schedule}```")
                embed3.set_author(name=f'{response.author}')
                embed3.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed3)
                await asyncio.sleep(1)
                #EXPERIENCE
                embed4 = discord.Embed(color=discord.Colour(0x0ab6ff), title=f"EVENT EXPERIENCE",
                description=f"\n__Do you have any previous experience in handling events?__\n```{experience}```")
                embed4.set_author(name=f'{response.author}')
                embed4.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed4)
                await asyncio.sleep(1)
                #SIGNORA
                embed5 = discord.Embed(color=discord.Colour(0x0ab6ff), title=f"SIGNORA",
                description=f"\n__What is your opinion of our Queen, Lady Signora?__\n```{signora}```")
                embed5.set_author(name=f'{response.author}')
                embed5.set_thumbnail(url=user.avatar_url)
                embed5.set_footer(text='Application for Cicin Mage | EVENT STAFF', icon_url='https://images.emojiterra.com/twitter/v13.0/512px/1f98b.png')
                await channel.send(embed=embed5)
                await channel.send('https://cdn.pixabay.com/photo/2017/03/18/21/29/divider-2154993_960_720.png')
                await asyncio.sleep(1)
                #RECEIPT
                await message.channel.send('Meeeeow nyan~!\n*Your application has been sent to the staff for review~!*\n**Here is your receipt**:')
                await asyncio.sleep(3)
                await message.channel.send(embed=embed1)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed2)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed3)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed4)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed5)
                await message.channel.send("**Thanks for applying!** โฅ")
              elif reaction.emoji == "๐":
#NSFW MOD                
                embed = discord.Embed(color=11534335, title = "Nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *How old are you?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=60.0, check=not_bot)
                age = response.content

                embed = discord.Embed(color=11534335, title = "Nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your timezone?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=60.0, check=not_bot)
                timezone = response.content

                embed = discord.Embed(color=11534335, title = "Nyan, nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Tell us about yourself, so we can get to know you better.*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=1200.0, check=not_bot)
                about_yourself = response.content

                embed = discord.Embed(color=11534335, title = "Nyan? Nya nyan nya nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your schedule like? How much time are you going to contribute?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                schedule = response.content

                embed = discord.Embed(color=11534335, title = "Nyan? Nya nyan NSFW nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Why do you want to moderate our NSFW category?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                NSFW = response.content
                
                embed = discord.Embed(color=11534335, title = "Nyan, Signora-sama nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your opinion of our Queen, Lady Signora?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                signora = response.content
                #SEND EMBED TO CHANNEL
                #FIRST EMBED
                embed1 = discord.Embed(color=discord.Colour(0x7a0000), title=f"USER ID: `{response.author.id}`",
                description=f"**AGE**\n__How old are you?__\n```{age}```\n\n**TIMEZONE**\n__What is your timezone?__\n```{timezone}```")
                embed1.set_author(name=f'{response.author}')
                embed1.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed1)
                await asyncio.sleep(1)
                #ABOUT YOURSELF
                embed2 = discord.Embed(color=discord.Colour(0x7a0000), title=f"ABOUT ME",
                description=f"\n__Tell us about yourself, so we can get to know you better.__\n```{about_yourself}```")
                embed2.set_author(name=f'{response.author}')
                embed2.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed2)
                await asyncio.sleep(1)
                #SCHEDULE
                embed3 = discord.Embed(color=discord.Colour(0x7a0000), title=f"SCHEDULE",
                description=f"\n__What is your schedule like? How much time are you going to contribute?__\n```{schedule}```")
                embed3.set_author(name=f'{response.author}')
                embed3.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed3)
                await asyncio.sleep(1)
                #NSFW
                embed4 = discord.Embed(color=discord.Colour(0x7a0000), title=f"REASON",
                description=f"\n__Why do you want to moderate our NSFW category?__\n```{NSFW}```")
                embed4.set_author(name=f'{response.author}')
                embed4.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed4)
                await asyncio.sleep(1)
                #SIGNORA
                embed5 = discord.Embed(color=discord.Colour(0x7a0000), title=f"SIGNORA",
                description=f"\n__What is your opinion of our Queen, Lady Signora?__\n```{signora}```")
                embed5.set_author(name=f'{response.author}')
                embed5.set_thumbnail(url=user.avatar_url)
                embed5.set_footer(text='Application for Fatui Bouncer | EVENT STAFF', icon_url='https://creazilla-store.fra1.digitaloceanspaces.com/emojis/41997/no-one-under-eighteen-emoji-clipart-xl.png')
                await channel.send(embed=embed5)
                await channel.send('https://cdn.pixabay.com/photo/2017/03/18/21/29/divider-2154993_960_720.png')
                await asyncio.sleep(1)
                #RECEIPT
                await message.channel.send('Meeeeow nyan~!\n*Your application has been sent to the staff for review~!*\n**Here is your receipt**:')
                await asyncio.sleep(3)
                await message.channel.send(embed=embed1)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed2)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed3)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed4)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed5)
                await message.channel.send("**Thanks for applying!** โฅ")
#BOTH NSFW AND CICIN
              elif reaction.emoji == "๐ฑ":
                embed = discord.Embed(color=11534335, title = "Nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *How old are you?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=60.0, check=not_bot)
                age = response.content

                embed = discord.Embed(color=11534335, title = "Nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your timezone?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=60.0, check=not_bot)
                timezone = response.content

                embed = discord.Embed(color=11534335, title = "Nyan, nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Tell us about yourself, so we can get to know you better.*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=1200.0, check=not_bot)
                about_yourself = response.content

                embed = discord.Embed(color=11534335, title = "Nyan? Nya nyan nya nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your schedule like? How much time are you going to contribute?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                schedule = response.content

                embed = discord.Embed(color=11534335, title = "Nyan nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Do you have any previous experience in handling events?*")
                cat = await message.channel.send(embed=embed)
                await cat.add_reaction("โ")
                await cat.add_reaction("โ")
                reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)
                if reaction.emoji == "โ":
                  embed = discord.Embed(color=11534335, title = "Nyaan nya nya!", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Please tell us more about them!*")
                  await message.channel.send(embed=embed)
                  response = await self.bot.wait_for('message', timeout=1200.0, check=not_bot)
                  experience = response.content
                elif reaction.emoji == "โ":
                  embed = discord.Embed(color=11534335, title = "Nyaan nya nya?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What can you contribute to the event team?*")
                  await message.channel.send(embed=embed)
                  response = await self.bot.wait_for('message', timeout=1200.0, check=not_bot)
                  experience = response.content
                
                embed = discord.Embed(color=11534335, title = "Nyan? Nya nyan NSFW nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *Why do you want to moderate our NSFW category?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                NSFW = response.content
                
                embed = discord.Embed(color=11534335, title = "Nyan, Signora-sama nyan?", description = "๐๐ซ๐๐ง๐ฌ๐ฅ๐๐ญ๐ข๐จ๐ง: *What is your opinion of our Queen, Lady Signora?*")
                await message.channel.send(embed=embed)
                response = await self.bot.wait_for('message', timeout=600.0, check=not_bot)
                signora = response.content
                #SEND EMBED TO CHANNEL
                #FIRST EMBED
                embed1 = discord.Embed(color=1, title=f"USER ID: `{response.author.id}`",
                description=f"**AGE**\n__How old are you?__\n```{age}```\n\n**TIMEZONE**\n__What is your timezone?__\n```{timezone}```")
                embed1.set_author(name=f'{response.author}')
                embed1.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed1)
                await asyncio.sleep(1)
                #ABOUT YOURSELF
                embed2 = discord.Embed(color=1, title=f"ABOUT ME",
                description=f"\n__Tell us about yourself, so we can get to know you better.__\n```{about_yourself}```")
                embed2.set_author(name=f'{response.author}')
                embed2.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed2)
                await asyncio.sleep(1)
                #SCHEDULE
                embed3 = discord.Embed(color=1, title=f"SCHEDULE",
                description=f"\n__What is your schedule like? How much time are you going to contribute?__\n```{schedule}```")
                embed3.set_author(name=f'{response.author}')
                embed3.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed3)
                await asyncio.sleep(1)
                #EXPERIENCE
                embed4 = discord.Embed(color=1, title=f"EVENT EXPERIENCE",
                description=f"\n__Do you have any previous experience in handling events?__\n```{experience}```")
                embed4.set_author(name=f'{response.author}')
                embed4.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed4)
                await asyncio.sleep(1)
                #NSFW
                embed5 = discord.Embed(color=1, title=f"REASON",
                description=f"\n__Why do you want to moderate our NSFW category?__\n```{NSFW}```")
                embed5.set_author(name=f'{response.author}')
                embed5.set_thumbnail(url=user.avatar_url)
                await channel.send(embed=embed5)
                await asyncio.sleep(1)
                #SIGNORA
                embed6 = discord.Embed(color=1, title=f"SIGNORA",
                description=f"\n__What is your opinion of our Queen, Lady Signora?__\n```{signora}```")
                embed6.set_author(name=f'{response.author}')
                embed6.set_thumbnail(url=user.avatar_url)
                embed6.set_footer(text='Application for Cicin Mage & Fatui Bouncer | STAFF', icon_url='https://www.transparentpng.com/thumb/8-ball-pool/eY1gZ7-8-ball-pool-picture.png')
                await channel.send(embed=embed6)
                await channel.send('https://cdn.pixabay.com/photo/2017/03/18/21/29/divider-2154993_960_720.png')
                await asyncio.sleep(1)
                #RECEIPT
                await message.channel.send('Meeeeow nyan~!\n*Your application has been sent to the staff for review~!*\n**Here is your receipt**:')
                await asyncio.sleep(3)
                await message.channel.send(embed=embed1)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed2)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed3)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed4)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed5)
                await asyncio.sleep(1)
                await message.channel.send(embed=embed6)
                await message.channel.send("**Thanks for applying!** โฅ")
              elif reaction.emoji == "โ":
                embed = discord.Embed(color=11014160, title="Nyan~", description='"*See you~*"')
                await cat.edit(embed=embed)       
            except asyncio.exceptions.TimeoutError:
              print("timeout error")
              self.bot.sent_event_message.remove(message.author.id)
              embed = discord.Embed(color=11014160, title="Nyan nyan (Bye bye)~ โซ")
              embed.set_footer(text = "Your request has timed out! Please try again.")
              await cat.edit(embed=embed)
            except:
              await message.channel.send('You probably typed too many characters. Max is 4000 characters each question!')
            else:
              print("success!")
              self.bot.sent_event_message.remove(message.author.id)
#------------------------------------------------
def setup(bot):
    bot.add_cog(ModApps(bot))