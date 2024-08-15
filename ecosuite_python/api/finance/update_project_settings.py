from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.project_finance_settings import ProjectFinanceSettings
from ...models.update_project_settings_response_200 import UpdateProjectSettingsResponse200
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ProjectFinanceSettings,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/finance/projects/{project_id}/settings",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UpdateProjectSettingsResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UpdateProjectSettingsResponse200.from_dict(response.json())

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
) -> Response[Union[Error, UpdateProjectSettingsResponse200]]:
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
    body: ProjectFinanceSettings,
) -> Response[Union[Error, UpdateProjectSettingsResponse200]]:
    """Update the finance settings for a project

     Update the finance settings for a project

    Args:
        project_id (str):
        body (ProjectFinanceSettings): Refer to the /schemas/finance endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateProjectSettingsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectFinanceSettings,
) -> Optional[Union[Error, UpdateProjectSettingsResponse200]]:
    """Update the finance settings for a project

     Update the finance settings for a project

    Args:
        project_id (str):
        body (ProjectFinanceSettings): Refer to the /schemas/finance endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateProjectSettingsResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectFinanceSettings,
) -> Response[Union[Error, UpdateProjectSettingsResponse200]]:
    """Update the finance settings for a project

     Update the finance settings for a project

    Args:
        project_id (str):
        body (ProjectFinanceSettings): Refer to the /schemas/finance endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateProjectSettingsResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ProjectFinanceSettings,
) -> Optional[Union[Error, UpdateProjectSettingsResponse200]]:
    """Update the finance settings for a project

     Update the finance settings for a project

    Args:
        project_id (str):
        body (ProjectFinanceSettings): Refer to the /schemas/finance endpoint for the full JSON
            Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateProjectSettingsResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
