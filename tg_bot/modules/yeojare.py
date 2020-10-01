from telegram import Update, Message
from telegram.ext import run_async

from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher

@run_async
def elainabot(bot: Bot, update: Update, args):
   message.reply
    
__help__ = """
 A little bit of info on Yeojare.
 By the way, it's pronounced 'YOUGH-JA-REH'.
 
 - /elaina gives you information on @ElainaBot.
 - /roxy gives you information on @RoxineBot.
"""

__mod_name__ = "Yeojare"

ELAINA_HANDLER = DisableAbleCommandHandler("elaina", elainabot, pass_args=True)
ROXY_HANDLER = DisableAbleCommandHandler("roxy", roxybot, pass_args=True)

dispatcher.add_handler(ELAINA_HANDLER)
dispatcher.add_handler(ROXY_HANDLER)
