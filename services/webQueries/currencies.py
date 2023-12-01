from decimal import Decimal
import logging
from datetime import date
from typing import Literal

from httpx import AsyncClient, HTTPError, TimeoutException
from numpy import transpose

from services.webQueries.exceptions import ApiException, InvalidEndpoint
from services.webQueries.literals import *
from services.webQueries.validationModels import (
    VALIDATORS,
    ConvertEndpoint,
    HistoricalEndpoint,
    LiveEndpoint,
    TimeFrameEndpoint,
)
from services.db.main import DataBase


async def get_currencies(
    url: str,
    headers: dict,
    endpoint: Literal['live', 'convert', 'timeframe', 'historical'],
    parameters: dict = None,
) -> tuple:
    """Create get request to server api and validate it.

    Args:
        url (str): Api url
        headers (dict): Include secure key for api
        endpoint (Literal[live, convert, timeframe, historical]): Api endpoint
        parameters (dict, optional): response parameters ex.: {'to': 'USD', 'from': 'RUB'}. Defaults to None.

    Returns:
        tuple: status code + response(response can be changed if it any exception)
    """
    api_url = url + endpoint
    status_code = 0
    try:
        response = await AsyncClient().get(
            api_url, params=parameters, headers=headers, timeout=50
        )
    except TimeoutException as e:
        logging.error(f'ServerTimeoutError{e} - {api_url}{parameters}')
        status_code = 1
        response = 'Could not get a response from server. Try again later.'
    except HTTPError as e:
        logging.error(f'HTTPError{e} - {parameters}')
        status_code = 1
        response = 'An error during to connect the server.'
    else:
        deserialized_response = response.json()
        if not deserialized_response.get('success', 1):
            logging.error(
                ApiException(deserialized_response['error']['info'], {parameters})
            )
            status_code = 1
            response = 'Something went wrong'
        elif 'message' in deserialized_response:
            logging.error(
                ApiException(deserialized_response['error']['info'], {parameters})
            )
            status_code = 1
            response = 'Something went wrong'

    return status_code, response


def parse_quotes(
    data: str, endpoint: Literal['live', 'convert', 'timeframe', 'historical']
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


def format_data(
    validator: LiveEndpoint | ConvertEndpoint | TimeFrameEndpoint | HistoricalEndpoint,
    endpoint: Literal['live', 'convert', 'timeframe', 'historical'],
    user_id: int = None,
) -> str | tuple[list[date], list[list[Decimal]], list[str]]:
    """Based on the endpoint, separates the formatting logic, then formats the text to response to the user.

    Args:
        validator (LiveEndpoint | ConvertEndpoint | TimeFrameEndpoint | HistoricalEndpoint): Pydantic validator object
        endpoint (Literal[live, convert, timeframe, historical]): Api endpoint
        user_id (int, optional): User id to get rounding idx. Defaults to None.

    Raises:
        InvalidEndpoint: ...

    Returns:
        str | tuple[list[date], list[list[Decimal]], list[str]]: Formatted answer for tg bot | formatted data for graphic plotting
    """
    if user_id:
        rounding_idx = DataBase().get_user_settings(user_id)[1]
    if endpoint == 'live':
        answer = [LIVE.format(source=validator.source)]
        for quote in validator.quotes:
            currency_value = round(validator.quotes[quote], rounding_idx)
            answer.append(f'{quote[3:]} - {currency_value}')

        return '\n'.join(answer)

    elif endpoint == 'convert':
        answer = CONVERT.format(
            source_currency=validator.query.from_,
            required_currency=validator.query.to,
            amount=validator.query.amount,
            result=round(validator.result, rounding_idx),
        )
        return answer

    elif endpoint == 'timeframe':
        response = [validator.quotes[i] for i in validator.quotes]
        currencies = list(response[0].keys())
        dates_axis = [date for date in validator.quotes]
        rates_axis = []
        for date in response:
            rates_axis.append([date[currency] for currency in date])
        rates_axis = list(transpose(rates_axis))

        return dates_axis, rates_axis, currencies

    elif endpoint == 'historical':
        ...

    else:
        raise InvalidEndpoint(
            'Invalid endpoint',
            'Please enter valid endpoint, its should be "live", "convert", "timeframe"',
        )
