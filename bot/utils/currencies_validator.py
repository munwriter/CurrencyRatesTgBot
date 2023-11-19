from bot.misc.constants import *


def validate_currencies(text: str, single: bool = False) -> bool:
    """Checking type of message and validate it using list of currencies

    Args:
        text (str): message
        single (bool, optional): single curr or many. Defaults to False.

    Returns:
        bool: if all is ok returns true otherwise false
    """
    if isinstance(text, str):
        text = text.upper().split()
        if single and len(text) > 1:
            return False
        for i in text:
            if i not in CURRENCIES:
                return False
    return True
