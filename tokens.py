import requests
import re
import time
from errors import RefreshTokenException


class Token:
    def __init__(self, config):
        self._session = requests.Session()
        self._session.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'})
        self.config = config
        self._retries = 5
        self._timeout = 10
        self.url = 'https://twitter.com'

    def _request(self):
        for attempt in range(self._retries + 1):
            req = self._session.prepare_request(
                requests.Request('GET', self.url))
            try:
                r = self._session.send(
                    req, allow_redirects=True, timeout=self._timeout)
            except requests.exceptions.RequestException as exc:
                if attempt < self._retries:
                    retrying = ', retrying'
                else:
                    retrying = ''
                print(f'Error retrieving {req.url}: {exc!r}{retrying}')
            else:
                success, msg = (True, None)
                msg = f': {msg}' if msg else ''

                if success:
                    return r
            if attempt < self._retries:
                sleep_time = 2.0 * 2 ** attempt
                time.sleep(sleep_time)
        else:
            msg = f'{self._retries + 1} requests to {self.url} failed, giving up.'
            self.config.Guest_token = None
            raise RefreshTokenException(msg)

    def refresh(self):
        res = self._request()
        match = re.search(r'\("gt=(\d+);', res.text)
        if match:
            self.config.Guest_token = str(match.group(1))
        else:
            self.config.Guest_token = None
            raise RefreshTokenException(
                'Could not find the Guest token in HTML')
