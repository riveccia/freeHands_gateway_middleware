"""Sample API Client."""
# import asyncio
import logging
# import socket

import aiohttp
# import async_timeout

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class FreehandsApiClient:
    def __init__(
        self, username: str, password: str, session: aiohttp.ClientSession
    ) -> None:
        """Sample API Client."""
        self._username = username
        self._passeword = password
        self._session = session

    async def async_get_data(self) -> dict:
        """Get data from the API."""
        # url = "https://jsonplaceholder.typicode.com/posts/1"
        # return await self.api_wrapper("get", url)
        return "{ \"userId\": 1,\"id\": 1,\"title\": \"sunt aut facere repellat provident occaecati excepturi optio reprehenderit\",\"body\": \"quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto\" } "

    # async def async_set_title(self, value: str) -> None:
    #     """Get data from the API."""
    #     url = "https://jsonplaceholder.typicode.com/posts/1"
    #     await self.api_wrapper("patch", url, data={"title": value}, headers=HEADERS)

    # async def api_wrapper(
    #     self, method: str, url: str, data: dict = {}, headers: dict = {}
    # ) -> dict:
    #     """Get information from the API."""
    #     try:
    #         _LOGGER.info("Prima dello scatto")
    #         async with async_timeout.timeout(TIMEOUT):
    #             _LOGGER.info("Scatta?")
    #             if method == "get":
    #                 response = await self._session.get(url, headers=headers)
    #                 return await response.json()

    #             elif method == "put":
    #                 await self._session.put(url, headers=headers, json=data)

    #             elif method == "patch":
    #                 await self._session.patch(url, headers=headers, json=data)

    #             elif method == "post":
    #                 await self._session.post(url, headers=headers, json=data)

    #     except asyncio.TimeoutError as exception:
    #         _LOGGER.error(
    #             "Timeout error fetching information from %s - %s",
    #             url,
    #             exception,
    #         )

    #     except (KeyError, TypeError) as exception:
    #         _LOGGER.error(
    #             "Error parsing information from %s - %s",
    #             url,
    #             exception,
    #         )
    #     except (aiohttp.ClientError, socket.gaierror) as exception:
    #         _LOGGER.error(
    #             "Error fetching information from %s - %s",
    #             url,
    #             exception,
    #         )
    #     except Exception as exception:  # pylint: disable=broad-except
    #         _LOGGER.error("Something really wrong happened! - %s", exception)
