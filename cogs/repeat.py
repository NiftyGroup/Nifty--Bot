from discord.ext import commands


class Mimic:
    """Repeats text"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    async def repeat(self, *, text):
        """Copies your words"""
        await self.bot.say(text)


def setup(bot):
    n = Mimic(bot)
    bot.add_cog(n)
