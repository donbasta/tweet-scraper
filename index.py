import argparse

from dataclasses import dataclass
from typing import Optional

from src.scraper import run


@dataclass
class Config:
    Username: Optional[str] = None


def init(args):
    c = Config()
    c.Username = args.username
    return c


def options():
    ap = argparse.ArgumentParser(
        prog="tweet-scraper", usage="scrape tweet", description="scrape tweet")
    ap.add_argument("-u", "--username",
                    help="User of the tweets you want to scrape")

    args = ap.parse_args()
    return args


def main():
    args = options()
    c = init(args)
    run(c)


if __name__ == "__main__":
    main()
