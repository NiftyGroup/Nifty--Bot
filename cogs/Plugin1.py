import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stevo(self):
        """This Gives Ben's Oppinions!"""

        #Your code will go here
        await self.bot.say("Stevo Is Gay According To Ben")

def setup(bot):
    bot.add_cog(Mycog(bot))
