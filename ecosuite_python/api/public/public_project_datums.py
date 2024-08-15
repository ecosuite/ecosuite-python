from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.public_project_datums_preset import PublicProjectDatumsPreset
from ...models.public_project_datums_response_200 import PublicProjectDatumsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
    *,
    preset: PublicProjectDatumsPreset,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_preset = preset.value
    params["preset"] = json_preset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/public/energy/datums/projects/{project_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, PublicProjectDatumsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PublicProjectDatumsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, PublicProjectDatumsResponse200]]:
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
    preset: PublicProjectDatumsPreset,
) -> Response[Union[Error, PublicProjectDatumsResponse200]]:
    """List publicly accessible preset energy datums for a project

     List publicly accessible preset energy datums for a project, providing access to a set span of
    recent datums

    Args:
        project_id (str):
        preset (PublicProjectDatumsPreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PublicProjectDatumsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        preset=preset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    preset: PublicProjectDatumsPreset,
) -> Optional[Union[Error, PublicProjectDatumsResponse200]]:
    """List publicly accessible preset energy datums for a project

     List publicly accessible preset energy datums for a project, providing access to a set span of
    recent datums

    Args:
        project_id (str):
        preset (PublicProjectDatumsPreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PublicProjectDatumsResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        preset=preset,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    preset: PublicProjectDatumsPreset,
) -> Response[Union[Error, PublicProjectDatumsResponse200]]:
    """List publicly accessible preset energy datums for a project

     List publicly accessible preset energy datums for a project, providing access to a set span of
    recent datums

    Args:
        project_id (str):
        preset (PublicProjectDatumsPreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, PublicProjectDatumsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        preset=preset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    preset: PublicProjectDatumsPreset,
) -> Optional[Union[Error, PublicProjectDatumsResponse200]]:
    """List publicly accessible preset energy datums for a project

     List publicly accessible preset energy datums for a project, providing access to a set span of
    recent datums

    Args:
        project_id (str):
        preset (PublicProjectDatumsPreset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, PublicProjectDatumsResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            preset=preset,
        )
    ).parsed
