from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.service_request_generation import ServiceRequestGeneration
from ...models.service_request_google_document import ServiceRequestGoogleDocument
from ...types import Response


def _get_kwargs(
    service_request_id: str,
    *,
    body: ServiceRequestGeneration,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/service-requests/{service_request_id}/generate",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, ServiceRequestGoogleDocument]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ServiceRequestGoogleDocument.from_dict(response.json())

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
) -> Response[Union[Error, ServiceRequestGoogleDocument]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceRequestGeneration,
) -> Response[Union[Error, ServiceRequestGoogleDocument]]:
    """Generate a Google Documents service request.

     Generate a Google Documents service request.

    Args:
        service_request_id (str):
        body (ServiceRequestGeneration): Some information on who to share the new service request
            with.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ServiceRequestGoogleDocument]]
    """

    kwargs = _get_kwargs(
        service_request_id=service_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceRequestGeneration,
) -> Optional[Union[Error, ServiceRequestGoogleDocument]]:
    """Generate a Google Documents service request.

     Generate a Google Documents service request.

    Args:
        service_request_id (str):
        body (ServiceRequestGeneration): Some information on who to share the new service request
            with.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ServiceRequestGoogleDocument]
    """

    return sync_detailed(
        service_request_id=service_request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceRequestGeneration,
) -> Response[Union[Error, ServiceRequestGoogleDocument]]:
    """Generate a Google Documents service request.

     Generate a Google Documents service request.

    Args:
        service_request_id (str):
        body (ServiceRequestGeneration): Some information on who to share the new service request
            with.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, ServiceRequestGoogleDocument]]
    """

    kwargs = _get_kwargs(
        service_request_id=service_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_request_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ServiceRequestGeneration,
) -> Optional[Union[Error, ServiceRequestGoogleDocument]]:
    """Generate a Google Documents service request.

     Generate a Google Documents service request.

    Args:
        service_request_id (str):
        body (ServiceRequestGeneration): Some information on who to share the new service request
            with.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, ServiceRequestGoogleDocument]
    """

    return (
        await asyncio_detailed(
            service_request_id=service_request_id,
            client=client,
            body=body,
        )
    ).parsed
