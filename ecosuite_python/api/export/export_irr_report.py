from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    project_ids: str,
    columns: Union[Unset, str] = UNSET,
    include_project_breakdown: Union[Unset, bool] = UNSET,
    aggregate: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["projectIds"] = project_ids

    params["columns"] = columns

    params["includeProjectBreakdown"] = include_project_breakdown

    params["aggregate"] = aggregate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/finance/export/report",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
) -> Response[Union[Any, Error]]:
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
    columns: Union[Unset, str] = UNSET,
    include_project_breakdown: Union[Unset, bool] = UNSET,
    aggregate: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Error]]:
    """Generates an export of the multi project IRR report

     Generates an export of the multi project IRR report emailing it to the requsting recipient

    Args:
        project_ids (str):
        columns (Union[Unset, str]):
        include_project_breakdown (Union[Unset, bool]):
        aggregate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        project_ids=project_ids,
        columns=columns,
        include_project_breakdown=include_project_breakdown,
        aggregate=aggregate,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    columns: Union[Unset, str] = UNSET,
    include_project_breakdown: Union[Unset, bool] = UNSET,
    aggregate: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Generates an export of the multi project IRR report

     Generates an export of the multi project IRR report emailing it to the requsting recipient

    Args:
        project_ids (str):
        columns (Union[Unset, str]):
        include_project_breakdown (Union[Unset, bool]):
        aggregate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return sync_detailed(
        client=client,
        project_ids=project_ids,
        columns=columns,
        include_project_breakdown=include_project_breakdown,
        aggregate=aggregate,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    columns: Union[Unset, str] = UNSET,
    include_project_breakdown: Union[Unset, bool] = UNSET,
    aggregate: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Error]]:
    """Generates an export of the multi project IRR report

     Generates an export of the multi project IRR report emailing it to the requsting recipient

    Args:
        project_ids (str):
        columns (Union[Unset, str]):
        include_project_breakdown (Union[Unset, bool]):
        aggregate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error]]
    """

    kwargs = _get_kwargs(
        project_ids=project_ids,
        columns=columns,
        include_project_breakdown=include_project_breakdown,
        aggregate=aggregate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    project_ids: str,
    columns: Union[Unset, str] = UNSET,
    include_project_breakdown: Union[Unset, bool] = UNSET,
    aggregate: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Error]]:
    """Generates an export of the multi project IRR report

     Generates an export of the multi project IRR report emailing it to the requsting recipient

    Args:
        project_ids (str):
        columns (Union[Unset, str]):
        include_project_breakdown (Union[Unset, bool]):
        aggregate (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_ids=project_ids,
            columns=columns,
            include_project_breakdown=include_project_breakdown,
            aggregate=aggregate,
        )
    ).parsed
