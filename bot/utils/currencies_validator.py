from bot.misc.constants import *


def validate_currencies(text: any, single: bool = False) -> bool:
    if isinstance(text, str):
        text = text.upper().split()
        if single and len(text) > 1:
            return False
        for i in text:
            if i not in CURRENCIES:
                return False
    return True
