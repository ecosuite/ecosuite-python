from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_service_request_response_200 import CreateServiceRequestResponse200
from ...models.error import Error
from ...models.service_request import ServiceRequest
from ...types import Response


def _get_kwargs(
    *,
    body: ServiceRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/service-requests",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateServiceRequestResponse200, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateServiceRequestResponse200.from_dict(response.json())

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
) -> Response[Union[CreateServiceRequestResponse200, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceRequest,
) -> Response[Union[CreateServiceRequestResponse200, Error]]:
    """Create a new serviceRequest

     Creates a new serviceRequest generating it a unique ID

    Args:
        body (ServiceRequest): Refer to the /schemas/service-request endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateServiceRequestResponse200, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ServiceRequest,
) -> Optional[Union[CreateServiceRequestResponse200, Error]]:
    """Create a new serviceRequest

     Creates a new serviceRequest generating it a unique ID

    Args:
        body (ServiceRequest): Refer to the /schemas/service-request endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateServiceRequestResponse200, Error]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceRequest,
) -> Response[Union[CreateServiceRequestResponse200, Error]]:
    """Create a new serviceRequest

     Creates a new serviceRequest generating it a unique ID

    Args:
        body (ServiceRequest): Refer to the /schemas/service-request endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateServiceRequestResponse200, Error]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ServiceRequest,
) -> Optional[Union[CreateServiceRequestResponse200, Error]]:
    """Create a new serviceRequest

     Creates a new serviceRequest generating it a unique ID

    Args:
        body (ServiceRequest): Refer to the /schemas/service-request endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateServiceRequestResponse200, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
