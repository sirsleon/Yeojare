import random
from typing import Optional, List

from telegram import Message, Update, Bot, User, ParseMode, Chat
from telegram.ext import Filters, MessageHandler, run_async

from tg_bot import dispatcher, LOGGER
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.string_handling import remove_emoji
from tg_bot.modules.translations.strings import tld, tld_list

from googletrans import LANGUAGES, Translator

@run_async
def do_translate(bot: Bot, update: Update, args: List[str]):
    chat = update.effective_chat  # type: Optional[Chat]
    msg = update.effective_message  # type: Optional[Message]
    lan = " ".join(args)

    if msg.reply_to_message and (msg.reply_to_message.audio
                                 or msg.reply_to_message.voice) or (
                                     args and args[0] == 'animal'):
        reply = random.choice(tld_list(chat.id, 'translator_animal_lang'))

        if args:
            translation_type = "text"
        else:
            translation_type = "audio"

        msg.reply_text(tld(chat.id, 'translator_animal_translated').format(
            translation_type, reply),
                       parse_mode=ParseMode.MARKDOWN)
        return

    if msg.reply_to_message:
        to_translate_text = remove_emoji(msg.reply_to_message.text)
    else:
        msg.reply_text(tld(chat.id, "Reply to a message to translate!"))
        return

    if not args:
        msg.reply_text(tld(chat.id, "Specify the language you want to translate the replied message to!"))
        return

    translator = Translator()
    try:
        translated = translator.translate(to_translate_text, dest=lan)
    except ValueError as e:
        msg.reply_text(tld(chat.id, "Error occured while translating:\n{}").format(e))

    src_lang = LANGUAGES[f'{translated.src.lower()}'].title()
    dest_lang = LANGUAGES[f'{translated.dest.lower()}'].title()
    translated_text = translated.text
    msg.reply_text(tld(chat.id,
                       "Source (`{}`):\n{} \n Destination (`{}`): \n{}").format(src_lang,
                                                       to_translate_text,
                                                       dest_lang,
                                                       translated_text),
                   parse_mode=ParseMode.MARKDOWN)

__help__ = """- /tr (language code) as reply to a long message.
"""
__mod_name__ = "Translator"

DO_TRANSLATE_HANDLER = DisableAbleCommandHandler("tr", do_translate, pass_args=True)

dispatcher.add_handler(DO_TRANSLATE_HANDLER)
