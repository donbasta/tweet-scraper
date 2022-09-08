from selenium.webdriver.common.by import By


def process_container(tweet_container):
    children = tweet_container.find_elements(By.XPATH, ".//*")
    tweet_tokens = []
    for c in children:
        if c.tag_name == "span":
            tweet_tokens.append(c.text)
        # elif c.tag_name == "div":
        #     link = c.find_elements(By.XPATH, ".//span/a")
        #     print(len(link))
        #     tweet_text.append(link[0].text)
    return "".join(tweet_tokens)
