from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.update_user_type_response_200 import UpdateUserTypeResponse200
from ...models.user_type import UserType
from ...types import Response


def _get_kwargs(
    user_type_id: str,
    *,
    body: UserType,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/user-types/{user_type_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UpdateUserTypeResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateUserTypeResponse200.from_dict(response.json())

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
) -> Response[Union[Error, UpdateUserTypeResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_type_id: str,
    *,
    client: AuthenticatedClient,
    body: UserType,
) -> Response[Union[Error, UpdateUserTypeResponse200]]:
    """Update the user type

     Update the user type

    Args:
        user_type_id (str):
        body (UserType): Refer to the /schemas/user-type endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateUserTypeResponse200]]
    """

    kwargs = _get_kwargs(
        user_type_id=user_type_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_type_id: str,
    *,
    client: AuthenticatedClient,
    body: UserType,
) -> Optional[Union[Error, UpdateUserTypeResponse200]]:
    """Update the user type

     Update the user type

    Args:
        user_type_id (str):
        body (UserType): Refer to the /schemas/user-type endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateUserTypeResponse200]
    """

    return sync_detailed(
        user_type_id=user_type_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    user_type_id: str,
    *,
    client: AuthenticatedClient,
    body: UserType,
) -> Response[Union[Error, UpdateUserTypeResponse200]]:
    """Update the user type

     Update the user type

    Args:
        user_type_id (str):
        body (UserType): Refer to the /schemas/user-type endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateUserTypeResponse200]]
    """

    kwargs = _get_kwargs(
        user_type_id=user_type_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_type_id: str,
    *,
    client: AuthenticatedClient,
    body: UserType,
) -> Optional[Union[Error, UpdateUserTypeResponse200]]:
    """Update the user type

     Update the user type

    Args:
        user_type_id (str):
        body (UserType): Refer to the /schemas/user-type endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateUserTypeResponse200]
    """

    return (
        await asyncio_detailed(
            user_type_id=user_type_id,
            client=client,
            body=body,
        )
    ).parsed
