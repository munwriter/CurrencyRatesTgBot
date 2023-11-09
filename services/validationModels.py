from pydantic import BaseModel, Field
from decimal import Decimal


class LiveEndpoint(BaseModel):
    quotes: dict[str, Decimal]
    source: str


class ConvertEndpointQuery(BaseModel):
    amount: Decimal
    from_: str = Field(..., alias='from')
    to: str


class ConvertEndpoint(BaseModel):
    query: ConvertEndpointQuery
    result: Decimal


class TimeFrameEndpoint(BaseModel):
    ...


class HistoricalEndpoint(BaseModel):
    ...


VALIDATORS = {
    'live': LiveEndpoint,
    'convert': ConvertEndpoint,
    'timeframe': TimeFrameEndpoint,
    'historical': HistoricalEndpoint
}
