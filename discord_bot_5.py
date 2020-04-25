import requests
from discord.ext import commands

TOKEN = BOT_TOKEN
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = TRANSLATOR_API_KEY


class TranslatorBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.lang = 'en-ru'

    @commands.command(name='set_lang')
    async def set_lang(self, ctx, lang):
        self.lang = lang
        await ctx.send('Type "!!text" and text for translate')

    @commands.command(name='help_bot')
    async def help(self, ctx):
        message = 'Commands:\n"!!set_lang" for language setting\n' \
                  '"!!text" for text to be translated'
        await ctx.send(message)

    @commands.command(name='text')
    async def translate(self, ctx, *text):
        params = {
            'key': API_KEY,
            'lang': self.lang,
            'text': ' '.join(text)
        }
        response = requests.get(URL, params=params).json()
        await ctx.send(' '.join(response['text']))


bot = commands.Bot(command_prefix='!!')
bot.add_cog(TranslatorBot(bot))
bot.run(TOKEN)
