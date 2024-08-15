from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.set_solar_node_credentials_body import SetSolarNodeCredentialsBody
from ...models.set_solar_node_credentials_proxy_url import SetSolarNodeCredentialsProxyUrl
from ...models.set_solar_node_credentials_response_200 import SetSolarNodeCredentialsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    body: SetSolarNodeCredentialsBody,
    node_id: str,
    proxy_url: SetSolarNodeCredentialsProxyUrl,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["nodeId"] = node_id

    json_proxy_url = proxy_url.value
    params["proxyUrl"] = json_proxy_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/solarnetwork/credentials/solarnode",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SetSolarNodeCredentialsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SetSolarNodeCredentialsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, SetSolarNodeCredentialsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SetSolarNodeCredentialsBody,
    node_id: str,
    proxy_url: SetSolarNodeCredentialsProxyUrl,
) -> Response[Union[Error, SetSolarNodeCredentialsResponse200]]:
    """Stores the user credentials for a Solar Node

     Stores the user credentials for a Solar Node

    Args:
        node_id (str):
        proxy_url (SetSolarNodeCredentialsProxyUrl):
        body (SetSolarNodeCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SetSolarNodeCredentialsResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        node_id=node_id,
        proxy_url=proxy_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SetSolarNodeCredentialsBody,
    node_id: str,
    proxy_url: SetSolarNodeCredentialsProxyUrl,
) -> Optional[Union[Error, SetSolarNodeCredentialsResponse200]]:
    """Stores the user credentials for a Solar Node

     Stores the user credentials for a Solar Node

    Args:
        node_id (str):
        proxy_url (SetSolarNodeCredentialsProxyUrl):
        body (SetSolarNodeCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SetSolarNodeCredentialsResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
        node_id=node_id,
        proxy_url=proxy_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SetSolarNodeCredentialsBody,
    node_id: str,
    proxy_url: SetSolarNodeCredentialsProxyUrl,
) -> Response[Union[Error, SetSolarNodeCredentialsResponse200]]:
    """Stores the user credentials for a Solar Node

     Stores the user credentials for a Solar Node

    Args:
        node_id (str):
        proxy_url (SetSolarNodeCredentialsProxyUrl):
        body (SetSolarNodeCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SetSolarNodeCredentialsResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        node_id=node_id,
        proxy_url=proxy_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SetSolarNodeCredentialsBody,
    node_id: str,
    proxy_url: SetSolarNodeCredentialsProxyUrl,
) -> Optional[Union[Error, SetSolarNodeCredentialsResponse200]]:
    """Stores the user credentials for a Solar Node

     Stores the user credentials for a Solar Node

    Args:
        node_id (str):
        proxy_url (SetSolarNodeCredentialsProxyUrl):
        body (SetSolarNodeCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SetSolarNodeCredentialsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            node_id=node_id,
            proxy_url=proxy_url,
        )
    ).parsed
