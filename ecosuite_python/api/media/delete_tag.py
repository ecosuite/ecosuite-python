from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_tag_response_200 import DeleteTagResponse200
from ...types import Response


def _get_kwargs(
    code: str,
    label: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/media/tags/storage/{code}/{label}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteTagResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteTagResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteTagResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteTagResponse200]:
    """Delete a media tag

     Delete a media tag

    Args:
        code (str):
        label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTagResponse200]
    """

    kwargs = _get_kwargs(
        code=code,
        label=label,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    code: str,
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteTagResponse200]:
    """Delete a media tag

     Delete a media tag

    Args:
        code (str):
        label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTagResponse200
    """

    return sync_detailed(
        code=code,
        label=label,
        client=client,
    ).parsed


async def asyncio_detailed(
    code: str,
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteTagResponse200]:
    """Delete a media tag

     Delete a media tag

    Args:
        code (str):
        label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteTagResponse200]
    """

    kwargs = _get_kwargs(
        code=code,
        label=label,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    code: str,
    label: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteTagResponse200]:
    """Delete a media tag

     Delete a media tag

    Args:
        code (str):
        label (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteTagResponse200
    """

    return (
        await asyncio_detailed(
            code=code,
            label=label,
            client=client,
        )
    ).parsed
