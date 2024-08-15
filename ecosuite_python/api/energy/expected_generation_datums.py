import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.expected_generation_datums_aggregation import ExpectedGenerationDatumsAggregation
from ...models.expected_generation_datums_response_200 import ExpectedGenerationDatumsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExpectedGenerationDatumsAggregation] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    json_aggregation: Union[Unset, str] = UNSET
    if not isinstance(aggregation, Unset):
        json_aggregation = aggregation.value

    params["aggregation"] = json_aggregation

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/energy/datums/generation/expected",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ExpectedGenerationDatumsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExpectedGenerationDatumsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, ExpectedGenerationDatumsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExpectedGenerationDatumsAggregation] = UNSET,
) -> Response[Union[Error, ExpectedGenerationDatumsResponse200]]:
    """List the expected generation energy datums for all projects

     List the expected generation energy datums for a specified date range and aggregate for all projects

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExpectedGenerationDatumsAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ExpectedGenerationDatumsResponse200]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        aggregation=aggregation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExpectedGenerationDatumsAggregation] = UNSET,
) -> Optional[Union[Error, ExpectedGenerationDatumsResponse200]]:
    """List the expected generation energy datums for all projects

     List the expected generation energy datums for a specified date range and aggregate for all projects

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExpectedGenerationDatumsAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ExpectedGenerationDatumsResponse200]
    """

    return sync_detailed(
        client=client,
        start=start,
        end=end,
        aggregation=aggregation,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExpectedGenerationDatumsAggregation] = UNSET,
) -> Response[Union[Error, ExpectedGenerationDatumsResponse200]]:
    """List the expected generation energy datums for all projects

     List the expected generation energy datums for a specified date range and aggregate for all projects

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExpectedGenerationDatumsAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ExpectedGenerationDatumsResponse200]]
    """

    kwargs = _get_kwargs(
        start=start,
        end=end,
        aggregation=aggregation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExpectedGenerationDatumsAggregation] = UNSET,
) -> Optional[Union[Error, ExpectedGenerationDatumsResponse200]]:
    """List the expected generation energy datums for all projects

     List the expected generation energy datums for a specified date range and aggregate for all projects

    Args:
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExpectedGenerationDatumsAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ExpectedGenerationDatumsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            start=start,
            end=end,
            aggregation=aggregation,
        )
    ).parsed
