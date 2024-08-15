from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_system_response_200 import CreateSystemResponse200
from ...models.error import Error
from ...models.system import System
from ...types import Response


def _get_kwargs(
    project_id: str,
    site_id: str,
    system_id: str,
    *,
    body: System,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/projects/{project_id}/sites/{site_id}/systems/{system_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateSystemResponse200, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateSystemResponse200.from_dict(response.json())

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
) -> Response[Union[CreateSystemResponse200, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    site_id: str,
    system_id: str,
    *,
    client: AuthenticatedClient,
    body: System,
) -> Response[Union[CreateSystemResponse200, Error]]:
    """Create a new system

     Create a new system with the specified ID

    Args:
        project_id (str):
        site_id (str):
        system_id (str):
        body (System): Refer to the /schemas/system endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateSystemResponse200, Error]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        site_id=site_id,
        system_id=system_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    site_id: str,
    system_id: str,
    *,
    client: AuthenticatedClient,
    body: System,
) -> Optional[Union[CreateSystemResponse200, Error]]:
    """Create a new system

     Create a new system with the specified ID

    Args:
        project_id (str):
        site_id (str):
        system_id (str):
        body (System): Refer to the /schemas/system endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSystemResponse200, Error]
    """

    return sync_detailed(
        project_id=project_id,
        site_id=site_id,
        system_id=system_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    site_id: str,
    system_id: str,
    *,
    client: AuthenticatedClient,
    body: System,
) -> Response[Union[CreateSystemResponse200, Error]]:
    """Create a new system

     Create a new system with the specified ID

    Args:
        project_id (str):
        site_id (str):
        system_id (str):
        body (System): Refer to the /schemas/system endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateSystemResponse200, Error]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        site_id=site_id,
        system_id=system_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    site_id: str,
    system_id: str,
    *,
    client: AuthenticatedClient,
    body: System,
) -> Optional[Union[CreateSystemResponse200, Error]]:
    """Create a new system

     Create a new system with the specified ID

    Args:
        project_id (str):
        site_id (str):
        system_id (str):
        body (System): Refer to the /schemas/system endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateSystemResponse200, Error]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            site_id=site_id,
            system_id=system_id,
            client=client,
            body=body,
        )
    ).parsed
