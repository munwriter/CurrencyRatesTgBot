from typing import Literal

from httpx import (
    AsyncClient,
    TimeoutException,
    ProtocolError,
    HTTPError
)

from .literals import *
from .exceptions import ApiException
from .validationModels import (
    VALIDATORS,
    LiveEndpoint,
    ConvertEndpoint,
    TimeFrameEndpoint,
    HistoricalEndpoint
)


async def get_currencies(url: str,
                         headers: dict,
                         endpoint: Literal['live', 'convert', 'timeframe', 'historical'],
                         parameters: dict = None,
                         ) -> str:
    """Create get request to server api and validate it.

    Args:
        url (str): Api url
        headers (dict): Include secure key for api
        endpoint (str): Api endpoint
        parameters (dict, optional): Response parameters ex.: {'to': 'USD', 'from': ''RUB}. Defaults to None.

    Raises:
        TimeoutException: if server don't get answer for a long time
        ProtocolError: Incorrect api ur
        HTTPError: Any error during to connect to the server
        ApiException: False success status
        ApiException: Any message from server

    Returns:
        str: Response in text(string) format
    """
    api_url = url + endpoint
    try:
        response = await AsyncClient().get(api_url,
                                           params=parameters,
                                           headers=headers)
    except TimeoutException:
        raise TimeoutException('Couldn`t get a response from server.')
    except ProtocolError:
        raise ProtocolError('Invalid url.')
    except HTTPError:
        raise HTTPError('An error during to connect the server.')

    deserialized_response = response.json()
    if deserialized_response.get('success', 1) == False:
        raise ApiException(deserialized_response['error']['info'])
    elif 'message' in deserialized_response:
        raise ApiException(deserialized_response['message'])

    return response.content


def parse_quotes(data: str,
                 endpoint: Literal['live', 'convert',
                                   'timeframe', 'historical']
                 ) -> LiveEndpoint | ConvertEndpoint | TimeFrameEndpoint | HistoricalEndpoint:
    """Get required validator from pydantic validators, deserialize data using this validator
    and returns validator object.

    Args:
        data (str): Text-format response
        endpoint (str): Api endpoint

    Returns:
        LiveEndpoint | ConvertEndpoint | TimeFrameEndpoint | HistoricalEndpoint: Pydantic validator object
    """
    validator = VALIDATORS[endpoint].model_validate_json(data)
    return validator


def format_data(validator: LiveEndpoint | ConvertEndpoint | TimeFrameEndpoint | HistoricalEndpoint,
                endpoint: Literal['live', 'convert', 'timeframe', 'historical']
                ) -> str:
    """Based on the endpoint, separates the formatting logic, then formats the text to response to the user.

    Args:
        validator (LiveEndpoint | ConvertEndpoint | TimeFrameEndpoint | HistoricalEndpoint): Pydantic validator object
        endpoint (str): Api endpoint

    Returns:
        str: Formatted answer for tg bot
    """
    if endpoint == 'live':
        answer = [LIVE.format(source=validator.source)]
        for quote in validator.quotes:
            answer.append(f'{quote[3:]} - {validator.quotes[quote]}')
        return '\n'.join(answer)

    elif endpoint == 'convert':
        answer = CONVERT.format(source_currency=validator.query.from_,
                                required_currency=validator.query.to,
                                amount=validator.query.amount,
                                result=validator.result)
        return answer

    elif endpoint == 'timeframe':
        ...

    elif endpoint == 'historical':
        ...

    else:
        raise Exception('Invalid endpoint')
