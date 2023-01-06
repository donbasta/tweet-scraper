# tweet-scraper

Literally a tweet-scraper

## Usage

1. First install the requirements from `requirements.txt`.
2. Install the corresponding webdriver (e.g. chromedriver for Google Chrome), and put it on your PATH because the scraper will try to invoke the chromedriver later
3. Create a .env file containing the following variables:

(update 23 Dec 2022: you can choose either one between email or username)

```env
TWITTER_LOGIN_EMAIL=example@gmail.com
TWITTER_LOGIN_USERNAME=example
TWITTER_LOGIN_PASSWORD=example
```

This allows the webdriver to login with your twitter credentials,
so you can scroll the twitter indefinitely without being prompted
to log in.

4. If you want to save the scrapped data, create directory `data` in the parent directory, and the scraped tweets will be saved there

5. Run the following script, where {twitter_username}
is the name of the twitter account whose tweets are to be scraped.
(without '@')

`python index.py -u {twitter_username}`

Example:

```bash
python index.py -u elonmusk
```

## How does it work

Twitter loads its page lazily, i.e. some of its content are dynamically generated
using AJAX calls, so one call HTTP GET request at the beginning will not work.
Instead, we need to simulate the loading process of the page like a browser, which can be done using selenium.

The browser will scroll down periodically to load and scrape older tweets,
and the script will try to find the HTML elements corresponding to tweets, parse them, and output them to the console.

## Todo:

* log in using account protected with 2fa
* add firefox option
* optimize scraping activity
