from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_sources_uses_mode import GetSourcesUsesMode
from ...models.sources_uses import SourcesUses
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    mode: Union[Unset, GetSourcesUsesMode] = UNSET,
    pro_forma_version_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_mode: Union[Unset, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params["proFormaVersionId"] = pro_forma_version_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/finance/sources-uses/{project_id}/sources-uses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SourcesUses]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SourcesUses.from_dict(response.json())

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
) -> Response[Union[Error, SourcesUses]]:
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
    mode: Union[Unset, GetSourcesUsesMode] = UNSET,
    pro_forma_version_id: Union[Unset, str] = UNSET,
) -> Response[Union[Error, SourcesUses]]:
    """Get the source and uses for a project

     Get the source and uses for a project

    Args:
        project_id (str):
        mode (Union[Unset, GetSourcesUsesMode]):
        pro_forma_version_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SourcesUses]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        mode=mode,
        pro_forma_version_id=pro_forma_version_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, GetSourcesUsesMode] = UNSET,
    pro_forma_version_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, SourcesUses]]:
    """Get the source and uses for a project

     Get the source and uses for a project

    Args:
        project_id (str):
        mode (Union[Unset, GetSourcesUsesMode]):
        pro_forma_version_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SourcesUses]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        mode=mode,
        pro_forma_version_id=pro_forma_version_id,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, GetSourcesUsesMode] = UNSET,
    pro_forma_version_id: Union[Unset, str] = UNSET,
) -> Response[Union[Error, SourcesUses]]:
    """Get the source and uses for a project

     Get the source and uses for a project

    Args:
        project_id (str):
        mode (Union[Unset, GetSourcesUsesMode]):
        pro_forma_version_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SourcesUses]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        mode=mode,
        pro_forma_version_id=pro_forma_version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, GetSourcesUsesMode] = UNSET,
    pro_forma_version_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, SourcesUses]]:
    """Get the source and uses for a project

     Get the source and uses for a project

    Args:
        project_id (str):
        mode (Union[Unset, GetSourcesUsesMode]):
        pro_forma_version_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SourcesUses]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            mode=mode,
            pro_forma_version_id=pro_forma_version_id,
        )
    ).parsed