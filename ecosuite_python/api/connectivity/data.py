import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.data_response_200 import DataResponse200
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_ird: Union[Unset, datetime.datetime] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_project_ird: Union[Unset, str] = UNSET
    if not isinstance(project_ird, Unset):
        json_project_ird = project_ird.isoformat()
    params["projectIrd"] = json_project_ird

    json_start = start.isoformat()
    params["start"] = json_start

    json_end = end.isoformat()
    params["end"] = json_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/connectivity/data",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DataResponse200, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataResponse200.from_dict(response.json())

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
) -> Response[Union[DataResponse200, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_ird: Union[Unset, datetime.datetime] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[DataResponse200, Error]]:
    """Lists the connectivity data for all projects

     Lists the connectivity data for all projects for the requested date range

    Args:
        project_ird (Union[Unset, datetime.datetime]):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataResponse200, Error]]
    """

    kwargs = _get_kwargs(
        project_ird=project_ird,
        start=start,
        end=end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_ird: Union[Unset, datetime.datetime] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[DataResponse200, Error]]:
    """Lists the connectivity data for all projects

     Lists the connectivity data for all projects for the requested date range

    Args:
        project_ird (Union[Unset, datetime.datetime]):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataResponse200, Error]
    """

    return sync_detailed(
        client=client,
        project_ird=project_ird,
        start=start,
        end=end,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_ird: Union[Unset, datetime.datetime] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Response[Union[DataResponse200, Error]]:
    """Lists the connectivity data for all projects

     Lists the connectivity data for all projects for the requested date range

    Args:
        project_ird (Union[Unset, datetime.datetime]):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DataResponse200, Error]]
    """

    kwargs = _get_kwargs(
        project_ird=project_ird,
        start=start,
        end=end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_ird: Union[Unset, datetime.datetime] = UNSET,
    start: datetime.datetime,
    end: datetime.datetime,
) -> Optional[Union[DataResponse200, Error]]:
    """Lists the connectivity data for all projects

     Lists the connectivity data for all projects for the requested date range

    Args:
        project_ird (Union[Unset, datetime.datetime]):
        start (datetime.datetime):
        end (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DataResponse200, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_ird=project_ird,
            start=start,
            end=end,
        )
    ).parsed
