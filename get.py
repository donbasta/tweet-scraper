from errors import TokenExpiryException
from json import loads
from async_timeout import timeout

import aiohttp
import url

httpproxy = None


def Limit(Limit, count):
    if Limit is not None and count >= int(Limit):
        return True


async def UserAgent():
    return "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36"


async def Request(_url, connector=None, params=None, headers=None):
    async with aiohttp.ClientSession(connector=connector, headers=headers) as session:
        return await Response(session, _url, params)


async def Response(session, _url, params=None):
    with timeout(120):
        async with session.get(_url, ssl=True, params=params, proxy=httpproxy) as response:
            resp = await response.text()
            if response.status == 429:
                raise TokenExpiryException(loads(resp)['errors'][0]['message'])
            return resp


async def RequestUrl(config, init):
    params = []
    _url = ""
    _headers = [("authorization", config.Bearer_token),
                ("x-guest-token", config.Guest_token)]
    _connector = None
    _url, params, _ = await url.Search(config, init)

    response = await Request(_url, params=params, connector=_connector, headers=_headers)

    return response
