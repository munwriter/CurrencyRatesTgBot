from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


class LiveEndpoint(BaseModel):
    quotes: dict[str, Decimal]
    source: str


class ConvertEndpointQuery(BaseModel):
    amount: Decimal
    from_: str = Field(..., alias="from")
    to: str


class ConvertEndpoint(BaseModel):
    query: ConvertEndpointQuery
    result: Decimal


class TimeFrameEndpoint(BaseModel):
    start_date: date
    end_date: date
    source: str
    quotes: dict[date, dict[str, Decimal]]


class HistoricalEndpoint(BaseModel):
    ...


VALIDATORS = {
    "live": LiveEndpoint,
    "convert": ConvertEndpoint,
    "timeframe": TimeFrameEndpoint,
    "historical": HistoricalEndpoint,
}
