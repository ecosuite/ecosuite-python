from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tags_response_200 import GetTagsResponse200
from ...types import Response


def _get_kwargs(
    code: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/media/tags/storage/code/{code}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTagsResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetTagsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTagsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetTagsResponse200]:
    """Get all media tags associated with a project code

     Get all media tags associated with a project code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsResponse200]
    """

    kwargs = _get_kwargs(
        code=code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetTagsResponse200]:
    """Get all media tags associated with a project code

     Get all media tags associated with a project code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsResponse200
    """

    return sync_detailed(
        code=code,
        client=client,
    ).parsed


async def asyncio_detailed(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetTagsResponse200]:
    """Get all media tags associated with a project code

     Get all media tags associated with a project code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTagsResponse200]
    """

    kwargs = _get_kwargs(
        code=code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    code: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetTagsResponse200]:
    """Get all media tags associated with a project code

     Get all media tags associated with a project code

    Args:
        code (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTagsResponse200
    """

    return (
        await asyncio_detailed(
            code=code,
            client=client,
        )
    ).parsed
