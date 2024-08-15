from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.lookup_address_business_details_body import LookupAddressBusinessDetailsBody
from ...models.lookup_address_business_details_response_200 import LookupAddressBusinessDetailsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: LookupAddressBusinessDetailsBody,
    radius: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["radius"] = radius

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/tools/address-business-details",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, LookupAddressBusinessDetailsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LookupAddressBusinessDetailsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, LookupAddressBusinessDetailsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LookupAddressBusinessDetailsBody,
    radius: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LookupAddressBusinessDetailsResponse200]]:
    """Look up the business details for supplied addresses

     Look up the business details for supplied addresses

    Args:
        radius (Union[Unset, str]):
        body (LookupAddressBusinessDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LookupAddressBusinessDetailsResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        radius=radius,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: LookupAddressBusinessDetailsBody,
    radius: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LookupAddressBusinessDetailsResponse200]]:
    """Look up the business details for supplied addresses

     Look up the business details for supplied addresses

    Args:
        radius (Union[Unset, str]):
        body (LookupAddressBusinessDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LookupAddressBusinessDetailsResponse200]
    """

    return sync_detailed(
        client=client,
        body=body,
        radius=radius,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LookupAddressBusinessDetailsBody,
    radius: Union[Unset, str] = UNSET,
) -> Response[Union[Error, LookupAddressBusinessDetailsResponse200]]:
    """Look up the business details for supplied addresses

     Look up the business details for supplied addresses

    Args:
        radius (Union[Unset, str]):
        body (LookupAddressBusinessDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, LookupAddressBusinessDetailsResponse200]]
    """

    kwargs = _get_kwargs(
        body=body,
        radius=radius,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LookupAddressBusinessDetailsBody,
    radius: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, LookupAddressBusinessDetailsResponse200]]:
    """Look up the business details for supplied addresses

     Look up the business details for supplied addresses

    Args:
        radius (Union[Unset, str]):
        body (LookupAddressBusinessDetailsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, LookupAddressBusinessDetailsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            radius=radius,
        )
    ).parsed
