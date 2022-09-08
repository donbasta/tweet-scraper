import sys
from asyncio import get_event_loop, set_event_loop, new_event_loop, ensure_future
import get
import utils
import tokens
from errors import NoMoreTweetsException, TokenExpiryException
import output

bearer = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs' \
         '%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'


class Scraper:
    def __init__(self, config):
        self.config = config
        self.count = 0
        self.feed = [-1]
        self.init = -1
        self.token = tokens.Token(config)
        self.token.refresh()
        self.config.Bearer_token = bearer

    async def main(self):
        task = ensure_future(self.run())
        await task

    async def Feed(self):
        while True:
            try:
                response = await get.RequestUrl(self.config, self.init)
            except TokenExpiryException as e:
                self.token.refresh()
                response = await get.RequestUrl(self.config, self.init)

            self.feed = []
            try:
                try:
                    self.feed, self.init = utils.parse_tweets(
                        self.config, response)
                except NoMoreTweetsException as e:
                    print(f'{e} -- Stopping scrapping...')
                    break
                break
            except TimeoutError as e:
                print(e)
                break
            except Exception as e:
                print(e)
        pass

    async def tweets(self):
        await self.Feed()
        for tweet in self.feed:
            self.count += 1
            await output.Tweets(tweet, self.config)

    async def run(self):
        self.user_agent = await get.UserAgent()

        while True:
            if len(self.feed) > 0:
                await self.tweets()
            else:
                break

            if get.Limit(self.config.Limit, self.count):
                break

        print(
            f"Finished scraping {self.count} tweets from username {self.config.Username}")


def Search(config):
    try:
        get_event_loop()
    except RuntimeError as e:
        if "no current event loop" in str(e):
            set_event_loop(new_event_loop())
        else:
            raise
    except Exception as e:
        sys.exit(0)

    get_event_loop().run_until_complete(Scraper(config).main())
