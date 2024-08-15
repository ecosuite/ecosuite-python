from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_finance_report_mode import GetFinanceReportMode
from ...models.get_finance_report_response_200 import GetFinanceReportResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_ids: str,
    aggregate: Union[Unset, str] = UNSET,
    mode: Union[Unset, GetFinanceReportMode] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["projectIds"] = project_ids

    params["aggregate"] = aggregate

    json_mode: Union[Unset, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/finance/report",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, GetFinanceReportResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetFinanceReportResponse200.from_dict(response.json())

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
) -> Response[Union[Error, GetFinanceReportResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    aggregate: Union[Unset, str] = UNSET,
    mode: Union[Unset, GetFinanceReportMode] = UNSET,
) -> Response[Union[Error, GetFinanceReportResponse200]]:
    """Get the finance report for a set of projects

     Get the finance report for a set of projects

    Args:
        project_ids (str):
        aggregate (Union[Unset, str]):
        mode (Union[Unset, GetFinanceReportMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetFinanceReportResponse200]]
    """

    kwargs = _get_kwargs(
        project_ids=project_ids,
        aggregate=aggregate,
        mode=mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    aggregate: Union[Unset, str] = UNSET,
    mode: Union[Unset, GetFinanceReportMode] = UNSET,
) -> Optional[Union[Error, GetFinanceReportResponse200]]:
    """Get the finance report for a set of projects

     Get the finance report for a set of projects

    Args:
        project_ids (str):
        aggregate (Union[Unset, str]):
        mode (Union[Unset, GetFinanceReportMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetFinanceReportResponse200]
    """

    return sync_detailed(
        client=client,
        project_ids=project_ids,
        aggregate=aggregate,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    aggregate: Union[Unset, str] = UNSET,
    mode: Union[Unset, GetFinanceReportMode] = UNSET,
) -> Response[Union[Error, GetFinanceReportResponse200]]:
    """Get the finance report for a set of projects

     Get the finance report for a set of projects

    Args:
        project_ids (str):
        aggregate (Union[Unset, str]):
        mode (Union[Unset, GetFinanceReportMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, GetFinanceReportResponse200]]
    """

    kwargs = _get_kwargs(
        project_ids=project_ids,
        aggregate=aggregate,
        mode=mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    aggregate: Union[Unset, str] = UNSET,
    mode: Union[Unset, GetFinanceReportMode] = UNSET,
) -> Optional[Union[Error, GetFinanceReportResponse200]]:
    """Get the finance report for a set of projects

     Get the finance report for a set of projects

    Args:
        project_ids (str):
        aggregate (Union[Unset, str]):
        mode (Union[Unset, GetFinanceReportMode]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, GetFinanceReportResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_ids=project_ids,
            aggregate=aggregate,
            mode=mode,
        )
    ).parsed
