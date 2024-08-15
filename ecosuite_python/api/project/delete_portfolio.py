from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_portfolio_response_200 import DeletePortfolioResponse200
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    portfolio_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/portfolios/{portfolio_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeletePortfolioResponse200, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeletePortfolioResponse200.from_dict(response.json())

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
) -> Response[Union[DeletePortfolioResponse200, Error]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeletePortfolioResponse200, Error]]:
    """Deletes an existing Portfolio

     Deletes an existing Portfolio

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeletePortfolioResponse200, Error]]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeletePortfolioResponse200, Error]]:
    """Deletes an existing Portfolio

     Deletes an existing Portfolio

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeletePortfolioResponse200, Error]
    """

    return sync_detailed(
        portfolio_id=portfolio_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[DeletePortfolioResponse200, Error]]:
    """Deletes an existing Portfolio

     Deletes an existing Portfolio

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeletePortfolioResponse200, Error]]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[DeletePortfolioResponse200, Error]]:
    """Deletes an existing Portfolio

     Deletes an existing Portfolio

    Args:
        portfolio_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeletePortfolioResponse200, Error]
    """

    return (
        await asyncio_detailed(
            portfolio_id=portfolio_id,
            client=client,
        )
    ).parsed
