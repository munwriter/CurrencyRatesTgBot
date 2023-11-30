GREETINGS_MESSAGE = '''We are glad to see you {name} in the our Telegram bot for tracking exchange rates.
Please choose the source currency.
It should be three-letters code.
<b>Ex("USD RUB PHP" | "EUR"| "PHP BTC").</b>'''
# ---------------------------------------------------------------------------------------------
ENTER_CURRENCY_MESSAGE = '''Now specify the currency you want to convert {direction}.
<b>It should be three-letters code.
Ex("USD" | "EUR"| "PHP")</b>'''
# ---------------------------------------------------------------------------------------------
INVALID_CURRENCY = '''Please enter valid currency!
<b>It should be three-letters code.
Ex("USD" | "EUR"| "PHP").</b>'''
# ---------------------------------------------------------------------------------------------
ENTER_DATE_MESSAGE = '''Enter the {option} date of your preferred timeframe.
<b>Maximum time frame is 365 days.
It should be YYYY-MM-DD format.
The start date should be less than the end date.
Ex(2020-05-01 | 2020-12-31 | 2007-05-29).</b>'''
# ---------------------------------------------------------------------------------------------
INVALID_DATE = '''Please enter valid date!
<b>Maximum time frame is 365 days.
It should be YYYY-MM-DD format.
The start date should be less than the end date.
Ex(2020-05-01 | 2020-12-31 | 2007-05-29).</b>'''
# ---------------------------------------------------------------------------------------------
CURRENCY_MESSAGE = '''Please choose the {option} currenc{singular_or_plural}.
<b>Separate currencies using whitespace
It should be three-letters code.
Ex("USD RUB PHP" | "EUR"| "PHP BTC").</b>'''
# ---------------------------------------------------------------------------------------------
TIMEFRAME_MESSAGE = '''Timeframe results:

<b>From:</b> {source_currency}
<b>To:</b> {required_currencies}
<b>Start date:</b> {start_date}
<b>End date:</b> {end_date}
<b>Timeframe:</b>'''
# ---------------------------------------------------------------------------------------------
USER_SETTINGS_MESSAGE = '''Your settings:

<b>Rounding index</b>: {rounding_idx}
<b>Source currency</b>: {source_cur}
<b>Required currencies</b>: {req_cur}
'''
# ---------------------------------------------------------------------------------------------
