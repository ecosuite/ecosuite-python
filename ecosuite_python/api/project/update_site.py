from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.site import Site
from ...models.update_site_response_200 import UpdateSiteResponse200
from ...types import Response


def _get_kwargs(
    project_id: str,
    site_id: str,
    *,
    body: Site,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/sites/{site_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UpdateSiteResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateSiteResponse200.from_dict(response.json())

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
) -> Response[Union[Error, UpdateSiteResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    body: Site,
) -> Response[Union[Error, UpdateSiteResponse200]]:
    """Update an existing site

     Update an existing site

    Args:
        project_id (str):
        site_id (str):
        body (Site): Refer to the /schemas/site endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateSiteResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        site_id=site_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    body: Site,
) -> Optional[Union[Error, UpdateSiteResponse200]]:
    """Update an existing site

     Update an existing site

    Args:
        project_id (str):
        site_id (str):
        body (Site): Refer to the /schemas/site endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateSiteResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        site_id=site_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    body: Site,
) -> Response[Union[Error, UpdateSiteResponse200]]:
    """Update an existing site

     Update an existing site

    Args:
        project_id (str):
        site_id (str):
        body (Site): Refer to the /schemas/site endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateSiteResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        site_id=site_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    site_id: str,
    *,
    client: AuthenticatedClient,
    body: Site,
) -> Optional[Union[Error, UpdateSiteResponse200]]:
    """Update an existing site

     Update an existing site

    Args:
        project_id (str):
        site_id (str):
        body (Site): Refer to the /schemas/site endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateSiteResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            site_id=site_id,
            client=client,
            body=body,
        )
    ).parsed
