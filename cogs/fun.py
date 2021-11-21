from discord.ext import commands
from dislash import *


class Fun(commands.Cog, description="Technical and Fun Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        for a in message.attachments:
            for e in ['3g2', '3gp', 'amv', 'asf', 'avi', 'drc', 'f4a', 'f4b', 'f4p', 'f4v', 'flv', 'gif', 'gifv',
                      'm2ts', 'm2v', 'm4p', 'm4v', 'mkv', 'mng', 'mov', 'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv',
                      'mts', 'mxf', 'nsv', 'ogg', 'ogv', 'qt', 'rm', 'rmvb', 'roq', 'svi', 'ts', 'vob', 'webm', 'wmv',
                      'yuv', 'mp3']:
                if a.filename[-len(e) - 1:] == f'.{e}':
                    await message.channel.send(
                        'https://i2.wp.com/www.betameme.com/wp-content/'
                        'uploads/2018/02/thank-you-meme-puppy.jpg?fit=498%2C462&ssl=1')
                    return

    @message_command(name='resend', guild_ids="770634445370687519")
    async def resend(self, inter):
        await inter.respond(f'{inter.message.content}')


def setup(bot):
    bot.add_cog(Fun(bot))
