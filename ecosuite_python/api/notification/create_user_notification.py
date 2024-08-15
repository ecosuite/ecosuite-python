from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_user_notification_response_200 import CreateUserNotificationResponse200
from ...models.error import Error
from ...models.user_notification import UserNotification
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    body: UserNotification,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/users/{user_id}/notifications",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateUserNotificationResponse200, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CreateUserNotificationResponse200.from_dict(response.json())

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
) -> Response[Union[CreateUserNotificationResponse200, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserNotification,
) -> Response[Union[CreateUserNotificationResponse200, Error]]:
    """Creates a new user notification

     Creates a new user notification

    Args:
        user_id (str):
        body (UserNotification): Refer to the /schemas/notification endpoint for the JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateUserNotificationResponse200, Error]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserNotification,
) -> Optional[Union[CreateUserNotificationResponse200, Error]]:
    """Creates a new user notification

     Creates a new user notification

    Args:
        user_id (str):
        body (UserNotification): Refer to the /schemas/notification endpoint for the JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateUserNotificationResponse200, Error]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserNotification,
) -> Response[Union[CreateUserNotificationResponse200, Error]]:
    """Creates a new user notification

     Creates a new user notification

    Args:
        user_id (str):
        body (UserNotification): Refer to the /schemas/notification endpoint for the JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateUserNotificationResponse200, Error]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: UserNotification,
) -> Optional[Union[CreateUserNotificationResponse200, Error]]:
    """Creates a new user notification

     Creates a new user notification

    Args:
        user_id (str):
        body (UserNotification): Refer to the /schemas/notification endpoint for the JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateUserNotificationResponse200, Error]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            body=body,
        )
    ).parsed
