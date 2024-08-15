from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.stop_ssh_session_response_200 import StopSshSessionResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    node_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["nodeId"] = node_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/solarnetwork/ssh",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, StopSshSessionResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = StopSshSessionResponse200.from_dict(response.json())

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
) -> Response[Union[Error, StopSshSessionResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    node_id: str,
) -> Response[Union[Error, StopSshSessionResponse200]]:
    """Stop existing SSH session to a Solar Node

     Stop existingSSH session to a Solar Node

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StopSshSessionResponse200]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    node_id: str,
) -> Optional[Union[Error, StopSshSessionResponse200]]:
    """Stop existing SSH session to a Solar Node

     Stop existingSSH session to a Solar Node

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StopSshSessionResponse200]
    """

    return sync_detailed(
        client=client,
        node_id=node_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    node_id: str,
) -> Response[Union[Error, StopSshSessionResponse200]]:
    """Stop existing SSH session to a Solar Node

     Stop existingSSH session to a Solar Node

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, StopSshSessionResponse200]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    node_id: str,
) -> Optional[Union[Error, StopSshSessionResponse200]]:
    """Stop existing SSH session to a Solar Node

     Stop existingSSH session to a Solar Node

    Args:
        node_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, StopSshSessionResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            node_id=node_id,
        )
    ).parsed
