import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.export_energy_aggregation import ExportEnergyAggregation
from ...models.export_energy_format import ExportEnergyFormat
from ...models.export_energy_response_200 import ExportEnergyResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_ids: str,
    source_ids: Union[Unset, str] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExportEnergyAggregation] = UNSET,
    format_: Union[Unset, ExportEnergyFormat] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["projectIds"] = project_ids

    params["sourceIds"] = source_ids

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    json_aggregation: Union[Unset, str] = UNSET
    if not isinstance(aggregation, Unset):
        json_aggregation = aggregation.value

    params["aggregation"] = json_aggregation

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/energy/export",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ExportEnergyResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExportEnergyResponse200.from_dict(response.json())

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
) -> Response[Union[Error, ExportEnergyResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    source_ids: Union[Unset, str] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExportEnergyAggregation] = UNSET,
    format_: Union[Unset, ExportEnergyFormat] = UNSET,
) -> Response[Union[Error, ExportEnergyResponse200]]:
    """Exports SolarNetwork datums

     Lists the instantaneous generation readings for every project

    Args:
        project_ids (str):
        source_ids (Union[Unset, str]):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExportEnergyAggregation]):
        format_ (Union[Unset, ExportEnergyFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ExportEnergyResponse200]]
    """

    kwargs = _get_kwargs(
        project_ids=project_ids,
        source_ids=source_ids,
        start=start,
        end=end,
        aggregation=aggregation,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    source_ids: Union[Unset, str] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExportEnergyAggregation] = UNSET,
    format_: Union[Unset, ExportEnergyFormat] = UNSET,
) -> Optional[Union[Error, ExportEnergyResponse200]]:
    """Exports SolarNetwork datums

     Lists the instantaneous generation readings for every project

    Args:
        project_ids (str):
        source_ids (Union[Unset, str]):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExportEnergyAggregation]):
        format_ (Union[Unset, ExportEnergyFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ExportEnergyResponse200]
    """

    return sync_detailed(
        client=client,
        project_ids=project_ids,
        source_ids=source_ids,
        start=start,
        end=end,
        aggregation=aggregation,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    source_ids: Union[Unset, str] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExportEnergyAggregation] = UNSET,
    format_: Union[Unset, ExportEnergyFormat] = UNSET,
) -> Response[Union[Error, ExportEnergyResponse200]]:
    """Exports SolarNetwork datums

     Lists the instantaneous generation readings for every project

    Args:
        project_ids (str):
        source_ids (Union[Unset, str]):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExportEnergyAggregation]):
        format_ (Union[Unset, ExportEnergyFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ExportEnergyResponse200]]
    """

    kwargs = _get_kwargs(
        project_ids=project_ids,
        source_ids=source_ids,
        start=start,
        end=end,
        aggregation=aggregation,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    source_ids: Union[Unset, str] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
    aggregation: Union[Unset, ExportEnergyAggregation] = UNSET,
    format_: Union[Unset, ExportEnergyFormat] = UNSET,
) -> Optional[Union[Error, ExportEnergyResponse200]]:
    """Exports SolarNetwork datums

     Lists the instantaneous generation readings for every project

    Args:
        project_ids (str):
        source_ids (Union[Unset, str]):
        start (datetime.datetime):
        end (datetime.datetime):
        aggregation (Union[Unset, ExportEnergyAggregation]):
        format_ (Union[Unset, ExportEnergyFormat]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ExportEnergyResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_ids=project_ids,
            source_ids=source_ids,
            start=start,
            end=end,
            aggregation=aggregation,
            format_=format_,
        )
    ).parsed
