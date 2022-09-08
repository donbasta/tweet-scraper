from urllib.parse import urlencode
from urllib.parse import quote

base = "https://api.twitter.com/2/search/adaptive.json"


def _sanitizeQuery(_url, params):
    _serialQuery = ""
    _serialQuery = urlencode(params, quote_via=quote)
    _serialQuery = _url + "?" + _serialQuery
    return _serialQuery


async def Search(config, init):
    url = base
    tweet_count = 100
    q = ""
    params = [
        ('include_can_media_tag', '1'),
        ('include_ext_alt_text', 'true'),
        ('include_quote_count', 'true'),
        ('include_reply_count', '1'),
        ('tweet_mode', 'extended'),
        ('include_entities', 'true'),
        ('include_user_entities', 'true'),
        ('include_ext_media_availability', 'true'),
        ('send_error_codes', 'true'),
        ('simple_quoted_tweet', 'true'),
        ('count', tweet_count),
        ('cursor', str(init)),
        ('spelling_corrections', '1'),
        ('ext', 'mediaStats%2ChighlightedLabel'),
        ('tweet_search_mode', 'live'),
    ]
    if config.Username:
        q += f" from:{config.Username}"

    q = q.strip()
    params.append(("q", q))
    _serialQuery = _sanitizeQuery(url, params)
    return url, params, _serialQuery
