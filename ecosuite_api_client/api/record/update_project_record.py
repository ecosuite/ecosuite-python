from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.record import Record
from ...models.update_project_record_response_200 import UpdateProjectRecordResponse200
from ...types import Response


def _get_kwargs(
    project_id: str,
    record_id: str,
    *,
    body: Record,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/projects/{project_id}/records/{record_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, UpdateProjectRecordResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateProjectRecordResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Error, UpdateProjectRecordResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
    body: Record,
) -> Response[Union[Error, UpdateProjectRecordResponse200]]:
    """Update an existing project record

     Update an existing project record

    Args:
        project_id (str):
        record_id (str):
        body (Record): Refer to the /schemas/record endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateProjectRecordResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        record_id=record_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
    body: Record,
) -> Optional[Union[Error, UpdateProjectRecordResponse200]]:
    """Update an existing project record

     Update an existing project record

    Args:
        project_id (str):
        record_id (str):
        body (Record): Refer to the /schemas/record endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateProjectRecordResponse200]
    """

    return sync_detailed(
        project_id=project_id,
        record_id=record_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
    body: Record,
) -> Response[Union[Error, UpdateProjectRecordResponse200]]:
    """Update an existing project record

     Update an existing project record

    Args:
        project_id (str):
        record_id (str):
        body (Record): Refer to the /schemas/record endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, UpdateProjectRecordResponse200]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        record_id=record_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    record_id: str,
    *,
    client: AuthenticatedClient,
    body: Record,
) -> Optional[Union[Error, UpdateProjectRecordResponse200]]:
    """Update an existing project record

     Update an existing project record

    Args:
        project_id (str):
        record_id (str):
        body (Record): Refer to the /schemas/record endpoint for the full JSON Schema definition

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, UpdateProjectRecordResponse200]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            record_id=record_id,
            client=client,
            body=body,
        )
    ).parsed
