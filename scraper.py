import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import StaleElementReferenceException

from constants import *
from utils import process_container


def initialize_driver():
    browser = webdriver.Chrome()
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
    time.sleep(1)

    body = browser.find_element(By.TAG_NAME, 'body')

    ts = "1h"
    while True:
        body.send_keys(Keys.PAGE_DOWN)

        tweet_containers = browser.find_elements(
            By.XPATH, TWEET_CONTAINER)
        for t in tweet_containers:
            try:
                content = t.find_element(
                    By.XPATH, ".//div[@data-testid='tweetText']")
                tweet_content = process_container(content)

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

        time.sleep(5)


def run(config):
    browser, wait = initialize_driver()
    login_twitter(browser, wait)
    search(browser, config.Username)
