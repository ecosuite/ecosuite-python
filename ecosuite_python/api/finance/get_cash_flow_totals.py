from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_cash_flow_totals_mode import GetCashFlowTotalsMode
from ...models.get_cash_flow_totals_response_200 import GetCashFlowTotalsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    mode: Union[Unset, GetCashFlowTotalsMode] = GetCashFlowTotalsMode.FORECAST,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_mode: Union[Unset, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/finance/cashflow-totals",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, GetCashFlowTotalsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCashFlowTotalsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, GetCashFlowTotalsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, GetCashFlowTotalsMode] = GetCashFlowTotalsMode.FORECAST,
) -> Response[Union[Error, GetCashFlowTotalsResponse200]]:
    """Get the cashflow totals for all projects

     Get the cashflow totals for all projects over their lifetime

    Args:
        mode (Union[Unset, GetCashFlowTotalsMode]):  Default: GetCashFlowTotalsMode.FORECAST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetCashFlowTotalsResponse200]]
    """

    kwargs = _get_kwargs(
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, GetCashFlowTotalsMode] = GetCashFlowTotalsMode.FORECAST,
) -> Optional[Union[Error, GetCashFlowTotalsResponse200]]:
    """Get the cashflow totals for all projects

     Get the cashflow totals for all projects over their lifetime

    Args:
        mode (Union[Unset, GetCashFlowTotalsMode]):  Default: GetCashFlowTotalsMode.FORECAST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetCashFlowTotalsResponse200]
    """

    return sync_detailed(
        client=client,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, GetCashFlowTotalsMode] = GetCashFlowTotalsMode.FORECAST,
) -> Response[Union[Error, GetCashFlowTotalsResponse200]]:
    """Get the cashflow totals for all projects

     Get the cashflow totals for all projects over their lifetime

    Args:
        mode (Union[Unset, GetCashFlowTotalsMode]):  Default: GetCashFlowTotalsMode.FORECAST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetCashFlowTotalsResponse200]]
    """

    kwargs = _get_kwargs(
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, GetCashFlowTotalsMode] = GetCashFlowTotalsMode.FORECAST,
) -> Optional[Union[Error, GetCashFlowTotalsResponse200]]:
    """Get the cashflow totals for all projects

     Get the cashflow totals for all projects over their lifetime

    Args:
        mode (Union[Unset, GetCashFlowTotalsMode]):  Default: GetCashFlowTotalsMode.FORECAST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetCashFlowTotalsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            mode=mode,
        )
    ).parsed
