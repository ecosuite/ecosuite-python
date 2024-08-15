from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    apply_changes: bool,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["applyChanges"] = apply_changes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/coda/{project_id}/import",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Error]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = Error.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    apply_changes: bool,
) -> Response[Error]:
    """Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

     Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

    Args:
        project_id (str):
        apply_changes (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        apply_changes=apply_changes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    apply_changes: bool,
) -> Optional[Error]:
    """Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

     Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

    Args:
        project_id (str):
        apply_changes (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        apply_changes=apply_changes,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    apply_changes: bool,
) -> Response[Error]:
    """Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

     Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

    Args:
        project_id (str):
        apply_changes (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        apply_changes=apply_changes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    apply_changes: bool,
) -> Optional[Error]:
    """Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

     Import Coda values using the Coda export spreadsheet in Google Spreadsheets.

    Args:
        project_id (str):
        apply_changes (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            apply_changes=apply_changes,
        )
    ).parsed
