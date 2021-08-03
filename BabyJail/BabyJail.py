import discord, asyncio
from discord.ext import commands

class BabyJail(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

#-------------------------------------
#BABY JAIL
  @commands.command(name="babyjail")
  @commands.has_role('Fatui Bouncer')
  async def babyjail(self, ctx: commands.Context, member: discord.Member):
    """
    Add a role to a member.
    `member` may be a member ID, mention, or name.
    `role` may be a role ID, mention, or name.
    """
    role = discord.utils.get(ctx.guild.roles,name="Baby Jail")
    channel = self.bot.get_channel(840432139304304708)
    if role in member.roles:
        await ctx.send(
            f"**{member}** already has the role **{role}**. Maybe try removing it instead."
        )
        return
    await member.add_roles(role)
    await ctx.send(f"Added **{role.name}** to **{member}**.")
    embed = discord.Embed(color=10158080, title="Baby Jailed", description=f"{ctx.author.mention} added **{role.name}** to **{member}**.")
    await channel.send(embed=embed)
  @babyjail.error
  async def points_error(self, ctx, error):
    if isinstance(error, commands.errors.MissingRole):
        await ctx.send('Only **Fatui Bouncers** can use this command!')

#----------------------------------------
def setup(bot):
  bot.add_cog(BabyJail(bot))
