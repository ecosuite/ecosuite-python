from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_cash_flow_payment_logs_response_200 import GetCashFlowPaymentLogsResponse200
from ...types import Response


def _get_kwargs(
    project_id: str,
    cash_flow_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/finance/projects/{project_id}/cash-flows/{cash_flow_id}/payment-logs",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, GetCashFlowPaymentLogsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetCashFlowPaymentLogsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, GetCashFlowPaymentLogsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    cash_flow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, GetCashFlowPaymentLogsResponse200]]:
    """Get the cash flow payment logs

     Get the cash flow payment logs for a specific cash flow in a project

    Args:
        project_id (str):
        cash_flow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetCashFlowPaymentLogsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cash_flow_id=cash_flow_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    cash_flow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, GetCashFlowPaymentLogsResponse200]]:
    """Get the cash flow payment logs

     Get the cash flow payment logs for a specific cash flow in a project

    Args:
        project_id (str):
        cash_flow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetCashFlowPaymentLogsResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        cash_flow_id=cash_flow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    cash_flow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Error, GetCashFlowPaymentLogsResponse200]]:
    """Get the cash flow payment logs

     Get the cash flow payment logs for a specific cash flow in a project

    Args:
        project_id (str):
        cash_flow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetCashFlowPaymentLogsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        cash_flow_id=cash_flow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    cash_flow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Error, GetCashFlowPaymentLogsResponse200]]:
    """Get the cash flow payment logs

     Get the cash flow payment logs for a specific cash flow in a project

    Args:
        project_id (str):
        cash_flow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetCashFlowPaymentLogsResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            cash_flow_id=cash_flow_id,
            client=client,
        )
    ).parsed
