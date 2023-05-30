from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import argparse


def main(args):
    URL = args.url
    timeout = args.timeout
    drivers = []

    for i in range(0,1):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--incognito")
        drivers.append(webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options))
        drivers[i].get(URL)
        action = ActionChains(drivers[i])
        action.send_keys(Keys.SPACE)
        action.perform()
        print("currently watching: "+URL)
        time.sleep(timeout)
        drivers[i].save_screenshot(str(time.time())+".png")
    
    print("watch done. program exited.")
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--timeout', type=int,
                    help='how long this app will run')
    parser.add_argument('--url', type=str,
                    help='video url that are going to be played')
    args = parser.parse_args()
    main(args)
