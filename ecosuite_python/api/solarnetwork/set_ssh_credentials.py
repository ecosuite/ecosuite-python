from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.set_ssh_credentials_body import SetSshCredentialsBody
from ...models.set_ssh_credentials_response_200 import SetSshCredentialsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: SetSshCredentialsBody,
    node_id: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["nodeId"] = node_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/solarnetwork/credentials/ssh",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SetSshCredentialsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SetSshCredentialsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, SetSshCredentialsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SetSshCredentialsBody,
    node_id: str,
) -> Response[Union[Error, SetSshCredentialsResponse200]]:
    """Stores the SSH credentials for a Solar Node

     Stores the SSH credentials for a Solar Node

    Args:
        node_id (str):
        body (SetSshCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SetSshCredentialsResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        node_id=node_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SetSshCredentialsBody,
    node_id: str,
) -> Optional[Union[Error, SetSshCredentialsResponse200]]:
    """Stores the SSH credentials for a Solar Node

     Stores the SSH credentials for a Solar Node

    Args:
        node_id (str):
        body (SetSshCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SetSshCredentialsResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
        node_id=node_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SetSshCredentialsBody,
    node_id: str,
) -> Response[Union[Error, SetSshCredentialsResponse200]]:
    """Stores the SSH credentials for a Solar Node

     Stores the SSH credentials for a Solar Node

    Args:
        node_id (str):
        body (SetSshCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SetSshCredentialsResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        node_id=node_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SetSshCredentialsBody,
    node_id: str,
) -> Optional[Union[Error, SetSshCredentialsResponse200]]:
    """Stores the SSH credentials for a Solar Node

     Stores the SSH credentials for a Solar Node

    Args:
        node_id (str):
        body (SetSshCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SetSshCredentialsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            node_id=node_id,
        )
    ).parsed
