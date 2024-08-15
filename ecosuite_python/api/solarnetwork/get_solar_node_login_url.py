from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_solar_node_login_url_proxy_url import GetSolarNodeLoginUrlProxyUrl
from ...models.get_solar_node_login_url_response_200 import GetSolarNodeLoginUrlResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    node_id: str,
    proxy_url: GetSolarNodeLoginUrlProxyUrl,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["nodeId"] = node_id

    json_proxy_url = proxy_url.value
    params["proxyUrl"] = json_proxy_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/solarnetwork/solarnode/login-url",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, GetSolarNodeLoginUrlResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetSolarNodeLoginUrlResponse200.from_dict(response.json())

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
) -> Response[Union[Error, GetSolarNodeLoginUrlResponse200]]:
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
    proxy_url: GetSolarNodeLoginUrlProxyUrl,
) -> Response[Union[Error, GetSolarNodeLoginUrlResponse200]]:
    """Gets a URL that can be used to login into a Solar Node

     Gets a URL that can be used to login into a Solar Node

    Args:
        node_id (str):
        proxy_url (GetSolarNodeLoginUrlProxyUrl):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetSolarNodeLoginUrlResponse200]]
    """

    kwargs = _get_kwargs(
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
    node_id: str,
    proxy_url: GetSolarNodeLoginUrlProxyUrl,
) -> Optional[Union[Error, GetSolarNodeLoginUrlResponse200]]:
    """Gets a URL that can be used to login into a Solar Node

     Gets a URL that can be used to login into a Solar Node

    Args:
        node_id (str):
        proxy_url (GetSolarNodeLoginUrlProxyUrl):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetSolarNodeLoginUrlResponse200]
    """

    return sync_detailed(
        client=client,
        node_id=node_id,
        proxy_url=proxy_url,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    node_id: str,
    proxy_url: GetSolarNodeLoginUrlProxyUrl,
) -> Response[Union[Error, GetSolarNodeLoginUrlResponse200]]:
    """Gets a URL that can be used to login into a Solar Node

     Gets a URL that can be used to login into a Solar Node

    Args:
        node_id (str):
        proxy_url (GetSolarNodeLoginUrlProxyUrl):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetSolarNodeLoginUrlResponse200]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        proxy_url=proxy_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    node_id: str,
    proxy_url: GetSolarNodeLoginUrlProxyUrl,
) -> Optional[Union[Error, GetSolarNodeLoginUrlResponse200]]:
    """Gets a URL that can be used to login into a Solar Node

     Gets a URL that can be used to login into a Solar Node

    Args:
        node_id (str):
        proxy_url (GetSolarNodeLoginUrlProxyUrl):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetSolarNodeLoginUrlResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            node_id=node_id,
            proxy_url=proxy_url,
        )
    ).parsed
