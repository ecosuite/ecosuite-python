from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.portfolio import Portfolio
from ...models.update_portfolio_response_200 import UpdatePortfolioResponse200
from ...types import Response


def _get_kwargs(
    portfolio_id: str,
    *,
    body: Portfolio,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/portfolios/{portfolio_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UpdatePortfolioResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdatePortfolioResponse200.from_dict(response.json())

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
) -> Response[Union[Error, UpdatePortfolioResponse200]]:
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
    body: Portfolio,
) -> Response[Union[Error, UpdatePortfolioResponse200]]:
    """Update an existing Portfolio

     Update an existing Portfolio

    Args:
        portfolio_id (str):
        body (Portfolio): Refer to the /schemas/portfolio endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdatePortfolioResponse200]]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
    body: Portfolio,
) -> Optional[Union[Error, UpdatePortfolioResponse200]]:
    """Update an existing Portfolio

     Update an existing Portfolio

    Args:
        portfolio_id (str):
        body (Portfolio): Refer to the /schemas/portfolio endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdatePortfolioResponse200]
    """

    return sync_detailed(
        portfolio_id=portfolio_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
    body: Portfolio,
) -> Response[Union[Error, UpdatePortfolioResponse200]]:
    """Update an existing Portfolio

     Update an existing Portfolio

    Args:
        portfolio_id (str):
        body (Portfolio): Refer to the /schemas/portfolio endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdatePortfolioResponse200]]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
    body: Portfolio,
) -> Optional[Union[Error, UpdatePortfolioResponse200]]:
    """Update an existing Portfolio

     Update an existing Portfolio

    Args:
        portfolio_id (str):
        body (Portfolio): Refer to the /schemas/portfolio endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdatePortfolioResponse200]
    """

    return (
        await asyncio_detailed(
            portfolio_id=portfolio_id,
            client=client,
            body=body,
        )
    ).parsed
