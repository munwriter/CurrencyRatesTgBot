from os import getenv
from typing import Literal

from services import currencies


async def request_currencies(endpoint: Literal['live', 'convert', 'timeframe', 'historical'], 
                             params: dict
                             ) -> str:
    """Entry point to make requests to api.

    Args:
        endpoint (str): Api endpoint
        params (dict): Request parameters

    Returns:
        str: Answer to tg bot
    """
    url = getenv('API_URL')
    headers = {'apikey': getenv('API_KEY')}
    server_response = await currencies.get_currencies(url, headers, endpoint, parameters=params)
    deserialized_response = currencies.parse_quotes(server_response, endpoint)
    answer = currencies.format_data(deserialized_response, endpoint)

    return answer
