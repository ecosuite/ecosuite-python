import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.site_weather_aggregation import SiteWeatherAggregation
from ...models.site_weather_response_200 import SiteWeatherResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    site_id: str,
    *,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, SiteWeatherAggregation] = UNSET,
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
        "url": f"/weather/projects/{project_id}/sites/{site_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SiteWeatherResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SiteWeatherResponse200.from_dict(response.json())

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
) -> Response[Union[Error, SiteWeatherResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, SiteWeatherAggregation] = UNSET,
) -> Response[Union[Error, SiteWeatherResponse200]]:
    """List the daylight readings for a project

     List the daylight readings for a specified date range and aggregate for a project

    Args:
        project_id (str):
        site_id (str):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, SiteWeatherAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SiteWeatherResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        site_id=site_id,
        start=start,
        end=end,
        aggregation=aggregation,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, SiteWeatherAggregation] = UNSET,
) -> Optional[Union[Error, SiteWeatherResponse200]]:
    """List the daylight readings for a project

     List the daylight readings for a specified date range and aggregate for a project

    Args:
        project_id (str):
        site_id (str):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, SiteWeatherAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SiteWeatherResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        site_id=site_id,
        client=client,
        start=start,
        end=end,
        aggregation=aggregation,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, SiteWeatherAggregation] = UNSET,
) -> Response[Union[Error, SiteWeatherResponse200]]:
    """List the daylight readings for a project

     List the daylight readings for a specified date range and aggregate for a project

    Args:
        project_id (str):
        site_id (str):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, SiteWeatherAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SiteWeatherResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        site_id=site_id,
        start=start,
        end=end,
        aggregation=aggregation,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, SiteWeatherAggregation] = UNSET,
) -> Optional[Union[Error, SiteWeatherResponse200]]:
    """List the daylight readings for a project

     List the daylight readings for a specified date range and aggregate for a project

    Args:
        project_id (str):
        site_id (str):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, SiteWeatherAggregation]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SiteWeatherResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            site_id=site_id,
            client=client,
            start=start,
            end=end,
            aggregation=aggregation,
        )
    ).parsed