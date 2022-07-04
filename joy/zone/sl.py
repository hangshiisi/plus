import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# start web browser
service = Service(executable_path="/home/aurora/workspace/bin/chromedriver")
browser = webdriver.Chrome(service=service)

# get source code
browser.get("https://en.wikipedia.org")
html = browser.page_source
time.sleep(2)
print(html)

# close web browser
browser.close()


