import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException

from constants import *
from utils import process_container

TWEET_HASHES = dict()


def get_browser_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("headless")
    return options


def initialize_driver():
    opt = get_browser_options()
    browser = webdriver.Chrome(chrome_options=opt)
    browser.maximize_window()
    wait = WebDriverWait(browser, 30)
    return browser, wait


def login_twitter(browser, wait):
    browser.get("https://twitter.com/login")
    print("waiting for the browser to load...")
    time.sleep(5)
    print("starting...")

    email_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "text")))
    email_input.send_keys('razudira282@gmail.com')

    next_button = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Next']")))
    next_button.click()

    time.sleep(2)

    uname_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "text")))
    uname_input.send_keys('benibokenda')

    next_button = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Next']")))
    next_button.click()

    password_input = wait.until(
        EC.visibility_of_element_located((By.NAME, "password")))
    password_input.send_keys('bethecoolguyya')

    login_button = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//span[text()='Log in']")))
    login_button.click()

    time.sleep(5)


def search(browser, username):
    base_url = u'https://twitter.com'
    url = f'{base_url}/{username}'

    browser.get(url)
    time.sleep(2)

    # body = browser.find_element(By.TAG_NAME, 'body')

    scroll_pause_time = 3
    screen_height = browser.execute_script("return window.screen.height;")
    # print(f"screen_height: {screen_height}")
    i = 1

    while True:
        # body.send_keys(Keys.PAGE_DOWN)
        browser.execute_script(
            f"window.scrollTo(0, {screen_height}*{i});")
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = browser.execute_script(
            "return document.body.scrollHeight;")
        # print(f"scroll_height: {scroll_height}")

        tweet_containers = browser.find_elements(
            By.XPATH, TWEET_CONTAINER)
        for t in tweet_containers:
            try:
                content = t.find_element(
                    By.XPATH, ".//div[@data-testid='tweetText']")
                tweet_content = process_container(content)

                h = hash(tweet_content)
                if h in TWEET_HASHES:
                    continue

                TWEET_HASHES[h] = True

                user = t.find_element(
                    By.XPATH, ".//div[@data-testid='User-Names']")
                username_element = user.find_element(
                    By.XPATH, ".//div[2]/div/div/a/div/span")

                uname = username_element.text
                # if uname != username:
                #     continue

                ts_element = t.find_element(
                    By.XPATH, ".//div[2]/div/div[3]/a/time")
                ts = ts_element.text

                print(f'<{uname} ({ts})>: {tweet_content}\n')

            except StaleElementReferenceException as e:
                print(e)

        if (screen_height) * i > scroll_height:
            break


def run(config):
    browser, wait = initialize_driver()
    login_twitter(browser, wait)
    search(browser, config.Username)
