from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_diff import AuditDiff
from ...models.audit_log import AuditLog
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    diff: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["diff"] = diff

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/audit/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, Union["AuditDiff", "AuditLog"]]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["AuditDiff", "AuditLog"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = AuditLog.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = AuditDiff.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[Error, Union["AuditDiff", "AuditLog"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    diff: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, Union["AuditDiff", "AuditLog"]]]:
    """Show audit logs for all user, user-group, user-type assests

     Specify diff to recevice a diff of the audit log changes

    Args:
        diff (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['AuditDiff', 'AuditLog']]]
    """

    kwargs = _get_kwargs(
        diff=diff,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    diff: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, Union["AuditDiff", "AuditLog"]]]:
    """Show audit logs for all user, user-group, user-type assests

     Specify diff to recevice a diff of the audit log changes

    Args:
        diff (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Union['AuditDiff', 'AuditLog']]
    """

    return sync_detailed(
        client=client,
        diff=diff,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    diff: Union[Unset, bool] = UNSET,
) -> Response[Union[Error, Union["AuditDiff", "AuditLog"]]]:
    """Show audit logs for all user, user-group, user-type assests

     Specify diff to recevice a diff of the audit log changes

    Args:
        diff (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, Union['AuditDiff', 'AuditLog']]]
    """

    kwargs = _get_kwargs(
        diff=diff,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    diff: Union[Unset, bool] = UNSET,
) -> Optional[Union[Error, Union["AuditDiff", "AuditLog"]]]:
    """Show audit logs for all user, user-group, user-type assests

     Specify diff to recevice a diff of the audit log changes

    Args:
        diff (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, Union['AuditDiff', 'AuditLog']]
    """

    return (
        await asyncio_detailed(
            client=client,
            diff=diff,
        )
    ).parsed
