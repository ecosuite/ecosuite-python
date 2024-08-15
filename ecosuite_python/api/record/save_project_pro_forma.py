from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.pro_forma import ProForma
from ...models.save_project_pro_forma_response_200 import SaveProjectProFormaResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    body: ProForma,
    version: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["version"] = version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/pro-forma",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SaveProjectProFormaResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SaveProjectProFormaResponse200.from_dict(response.json())

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
) -> Response[Union[Error, SaveProjectProFormaResponse200]]:
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
    body: ProForma,
    version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, SaveProjectProFormaResponse200]]:
    """Save Pro Forma details

     Saves the Pro Forma details for the specified project

    Args:
        project_id (str):
        version (Union[Unset, str]):
        body (ProForma): Refer to the /schemas/pro-forma endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SaveProjectProFormaResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ProForma,
    version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, SaveProjectProFormaResponse200]]:
    """Save Pro Forma details

     Saves the Pro Forma details for the specified project

    Args:
        project_id (str):
        version (Union[Unset, str]):
        body (ProForma): Refer to the /schemas/pro-forma endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SaveProjectProFormaResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
        version=version,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ProForma,
    version: Union[Unset, str] = UNSET,
) -> Response[Union[Error, SaveProjectProFormaResponse200]]:
    """Save Pro Forma details

     Saves the Pro Forma details for the specified project

    Args:
        project_id (str):
        version (Union[Unset, str]):
        body (ProForma): Refer to the /schemas/pro-forma endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SaveProjectProFormaResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient,
    body: ProForma,
    version: Union[Unset, str] = UNSET,
) -> Optional[Union[Error, SaveProjectProFormaResponse200]]:
    """Save Pro Forma details

     Saves the Pro Forma details for the specified project

    Args:
        project_id (str):
        version (Union[Unset, str]):
        body (ProForma): Refer to the /schemas/pro-forma endpoint for the full JSON Schema
            definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SaveProjectProFormaResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
            version=version,
        )
    ).parsed
