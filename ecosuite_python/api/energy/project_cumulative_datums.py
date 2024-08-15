import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.project_cumulative_datums_response_200 import ProjectCumulativeDatumsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    cumulative: datetime.datetime,
    cumulative_date: datetime.datetime,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_cumulative = cumulative.isoformat()
    params["cumulative"] = json_cumulative

    json_cumulative_date = cumulative_date.isoformat()
    params["cumulativeDate"] = json_cumulative_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/energy/datums/cumulative/projects/{project_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ProjectCumulativeDatumsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProjectCumulativeDatumsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, ProjectCumulativeDatumsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cumulative: datetime.datetime,
    cumulative_date: datetime.datetime,
) -> Response[Union[Error, ProjectCumulativeDatumsResponse200]]:
    """List the cumulative energy datums for a project

     List the cumulative energy datums for a specified cumulativefor a project

    Args:
        project_id (str):
        cumulative (datetime.datetime):
        cumulative_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ProjectCumulativeDatumsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cumulative=cumulative,
        cumulative_date=cumulative_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cumulative: datetime.datetime,
    cumulative_date: datetime.datetime,
) -> Optional[Union[Error, ProjectCumulativeDatumsResponse200]]:
    """List the cumulative energy datums for a project

     List the cumulative energy datums for a specified cumulativefor a project

    Args:
        project_id (str):
        cumulative (datetime.datetime):
        cumulative_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ProjectCumulativeDatumsResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        cumulative=cumulative,
        cumulative_date=cumulative_date,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cumulative: datetime.datetime,
    cumulative_date: datetime.datetime,
) -> Response[Union[Error, ProjectCumulativeDatumsResponse200]]:
    """List the cumulative energy datums for a project

     List the cumulative energy datums for a specified cumulativefor a project

    Args:
        project_id (str):
        cumulative (datetime.datetime):
        cumulative_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ProjectCumulativeDatumsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cumulative=cumulative,
        cumulative_date=cumulative_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    cumulative: datetime.datetime,
    cumulative_date: datetime.datetime,
) -> Optional[Union[Error, ProjectCumulativeDatumsResponse200]]:
    """List the cumulative energy datums for a project

     List the cumulative energy datums for a specified cumulativefor a project

    Args:
        project_id (str):
        cumulative (datetime.datetime):
        cumulative_date (datetime.datetime):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ProjectCumulativeDatumsResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            cumulative=cumulative,
            cumulative_date=cumulative_date,
        )
    ).parsed
