import argparse
import config
import scraper


def init(args):
    c = config.Config()
    c.Username = args.username
    c.Limit = args.limit
    return c


def options():
    ap = argparse.ArgumentParser(
        prog="tweet-scraper", usage="scrape tweet", description="scrape tweet")
    ap.add_argument("-u", "--username",
                    help="User of the tweets you want to scrape")
    ap.add_argument("-l", "--limit", help="Limit the number of tweets scraped")

    args = ap.parse_args()
    return args


def main():
    args = options()
    c = init(args)
    scraper.Search(c)
    pass


if __name__ == "__main__":
    main()
