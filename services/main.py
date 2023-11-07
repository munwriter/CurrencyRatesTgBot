from services import currencies
from os import getenv


async def request_currencies(endpoint: str, params: dict) -> str:
    """Entry point to make requests tp api.

    Args:
        endpoint (str): Api endpoint
        params (dict): Request parameters

    Returns:
        str: answer to tg bot
    """
    url = getenv('API_URL')
    headers = {'apikey': getenv('API_KEY')}
    server_response = await currencies.get_currencies(url, headers, endpoint, parameters=params)
    deserialized_response = currencies.parse_quotes(server_response, endpoint)
    answer = currencies.format_data(deserialized_response, endpoint)

    return answer
