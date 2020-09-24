from tg_bot.modules.sql.locales_sql import prev_locale
from tg_bot.modules.translations.English import EnglishStrings
from tg_bot.modules.translations.Russian import RussianStrings
from tg_bot.modules.translations.Ukraine import UkrainianStrings

def tld(chat_id, t, show_none=True):
    LANGUAGE = prev_locale(chat_id)
    print(chat_id, t)
    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name
        if LOCALE in ('ru') and t in RussianStrings:
           return RussianStrings[t]
        elif LOCALE in ('uk') and t in UkrainianStrings:
            return UkrainianStrings[t]
        else:
            if t in EnglishStrings:
                return EnglishStrings[t]
            else:
                return t
    elif show_none:
        if t in EnglishStrings:
            return EnglishStrings[t]
        else:
            return t

def tld_list(chat_id, t):
    LANGUAGE = prev_locale(chat_id)

    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name
        if LOCALE in ('en-US') and t in strings['en-US']:
            return strings['en-US'][t]
        elif LOCALE in ('en-GB') and t in strings['en-GB']:
            return strings['en-GB'][t]
        elif LOCALE in ('id') and t in strings['id']:
            return strings['id'][t]
        elif LOCALE in ('ru') and t in strings['ru']:
            return strings['ru'][t]
        elif LOCALE in ('es') and t in strings['es']:
            return strings['es'][t]

def tld_help(chat_id, t):
    LANGUAGE = prev_locale(chat_id)
    print("tld_help ", chat_id, t)
    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name

        t = t + "_help"

        print("Test2", t)

        if LOCALE in ('ru') and t in RussianStrings:
            return RussianStrings[t]
        elif LOCALE in ('uk') and t in UkrainianStrings:
            return UkrainianStrings[t]
        else:
            return False
    else:
        return False
