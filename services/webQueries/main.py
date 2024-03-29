from datetime import date
from decimal import Decimal
from os import getenv
from typing import Literal

from services.webQueries import currencies


async def request_currencies(
    endpoint: Literal['live', 'convert', 'timeframe', 'historical'],
    params: dict,
    user_id: int | None = None,
) -> str | tuple[list[date], list[list[Decimal]], list[str]]:
    """Entry point to make requests to api.

    Args:
        endpoint (str): Api endpoint
        params (dict): Request parameters

    Returns:
        str: Answer to tg bot
        tuple[list[date], list[list[Decimal]], list[str]]: formatted date for graphic plotting
    """
    url = getenv('API_URL')
    headers = {'apikey': getenv('API_KEY')}

    server_response = await currencies.get_currencies(
        url, headers, endpoint, parameters=params
    )
    if server_response[0]:
        return server_response[1]

    deserialized_response = currencies.parse_quotes(server_response[1].text, endpoint)
    answer = currencies.format_data(deserialized_response, endpoint, user_id)

    return answer
