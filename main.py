from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://v4.eccube-plugin.net/")
assert "workflows" in driver.title
driver.close()