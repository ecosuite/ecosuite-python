from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.send_feedback_response_200 import SendFeedbackResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    version: str,
    email: Union[Unset, str] = UNSET,
    feedback: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["version"] = version

    params["email"] = email

    params["feedback"] = feedback

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/feedback",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Error, SendFeedbackResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SendFeedbackResponse200.from_dict(response.json())

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
) -> Response[Union[Error, SendFeedbackResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    version: str,
    email: Union[Unset, str] = UNSET,
    feedback: str,
) -> Response[Union[Error, SendFeedbackResponse200]]:
    """Send some feedback

     Send some feedback

    Args:
        version (str):
        email (Union[Unset, str]):
        feedback (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SendFeedbackResponse200]]
    """

    kwargs = _get_kwargs(
        version=version,
        email=email,
        feedback=feedback,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    version: str,
    email: Union[Unset, str] = UNSET,
    feedback: str,
) -> Optional[Union[Error, SendFeedbackResponse200]]:
    """Send some feedback

     Send some feedback

    Args:
        version (str):
        email (Union[Unset, str]):
        feedback (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SendFeedbackResponse200]
    """

    return sync_detailed(
        client=client,
        version=version,
        email=email,
        feedback=feedback,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    version: str,
    email: Union[Unset, str] = UNSET,
    feedback: str,
) -> Response[Union[Error, SendFeedbackResponse200]]:
    """Send some feedback

     Send some feedback

    Args:
        version (str):
        email (Union[Unset, str]):
        feedback (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Error, SendFeedbackResponse200]]
    """

    kwargs = _get_kwargs(
        version=version,
        email=email,
        feedback=feedback,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    version: str,
    email: Union[Unset, str] = UNSET,
    feedback: str,
) -> Optional[Union[Error, SendFeedbackResponse200]]:
    """Send some feedback

     Send some feedback

    Args:
        version (str):
        email (Union[Unset, str]):
        feedback (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Error, SendFeedbackResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            version=version,
            email=email,
            feedback=feedback,
        )
    ).parsed
