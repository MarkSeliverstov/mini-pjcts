import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def send_telegram(text: str):
    # Send message in telegram by bot
    # enter bots token
    token = ""
    url = "https://api.telegram.org/bot"
    # enter bots channel_id
    channel_id = ""
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })
    if r.status_code != 200:
        raise Exception("post_text error")


def main():
    number_of_no = 0
    number_of_sent_no = 1
    driver = webdriver.Chrome()
    driver.get("https://frs.gov.cz/cs/ioff/month/2022-9")

    elem = driver.find_elements(By.ID, "edit-name--2")
    for e in elem:
        # enter your username here
        e.send_keys('<login>')

    pwd = driver.find_elements(By.ID, "edit-pass--2")
    for e in pwd:
        # enter your password here
        e.send_keys('<password>')

    driver.find_element(By.ID, "edit-submit--2").submit()
    print("login completed successfully")
    time.sleep(10)

    # Every 30 seconds the site is updated and a free space is searched for
    while True:
        if driver.find_elements(By.CLASS_NAME, "daynum"):
            print("yes")
            send_telegram("There is a free space")

        else:
            print("No [{}]".format(number_of_no))
            print("––––––")
            if number_of_no == 0:
                send_telegram("No [{}]".format(number_of_sent_no))
            elif number_of_no == 1000:
                number_of_no = 0
                number_of_sent_no += 1
            number_of_no += 1
        time.sleep(15)
        driver.refresh()


if __name__ == '__main__':
    main()
